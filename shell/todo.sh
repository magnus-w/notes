# todo.txt shell integration for the notes repo. Works under bash and zsh.
#
# Source this from ~/.bashrc or ~/.zshrc:
#   [ -r "$HOME/GitHub/notes/shell/todo.sh" ] && . "$HOME/GitHub/notes/shell/todo.sh"
#
# This file is the single source of truth for both machines — edit it here,
# commit, and pull elsewhere. Nothing below hardcodes the repo path.

# Repo root, derived from this file's own location.
if [ -n "$ZSH_VERSION" ]; then
  NOTES_REPO=${${(%):-%x}:A:h:h}
else
  NOTES_REPO=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
fi
export NOTES_REPO
export TODOTXT_CFG_FILE="$NOTES_REPO/shell/todo.cfg"

alias todo='todo.sh'

# Completion ships with todo.txt-cli but lands in a different place on every
# platform, so take the first one that exists. zsh needs the bash compat layer.
if [ -n "$ZSH_VERSION" ]; then
  autoload -U +X bashcompinit && bashcompinit
fi
for _todo_compl in /opt/homebrew/etc/bash_completion.d/todo_completion \
                   /usr/local/etc/bash_completion.d/todo_completion \
                   /usr/share/bash-completion/completions/todo_completion \
                   /etc/bash_completion.d/todo_completion \
                   "$HOME/.local/bin/todo_completion"; do
  if [ -r "$_todo_compl" ]; then
    . "$_todo_compl"
    complete -F _todo todo 2>/dev/null
    break
  fi
done
unset _todo_compl

# Sync the whole notes repo. Task changes are committed separately from
# everything else, so todo churn doesn't bury real note edits in the log.
todoc() {
  local repo="$NOTES_REPO" stamp
  stamp=$(date '+%Y-%m-%d %H:%M')

  git -C "$repo" add todo || return 1
  git -C "$repo" diff --cached --quiet -- todo \
    || git -C "$repo" commit -q -m "todo: update $stamp" -- todo || return 1

  # Sweep up notes edited elsewhere (Zed, etc.) and forgotten.
  git -C "$repo" add -A || return 1
  git -C "$repo" diff --cached --quiet \
    || git -C "$repo" commit -q -m "notes: sync $stamp" || return 1

  # Task files union-merge via .gitattributes, so same-day edits on two
  # machines combine cleanly. Anything else that conflicts is backed out
  # rather than left half-rebased.
  if ! git -C "$repo" pull --rebase --autostash -q; then
    git -C "$repo" rebase --abort 2>/dev/null
    echo "todoc: conflict — repo left untouched, resolve by hand in $repo" >&2
    return 1
  fi
  git -C "$repo" push -q && echo "todo: synced"
}

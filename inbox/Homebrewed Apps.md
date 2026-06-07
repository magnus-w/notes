# Home brewed apps and productivity

- As you wrote about in a Verge article, with Claude Code we can build our own custom apps.

- And in a previous Installer you told the inspiring story of how you built an app that glues Obsidian and other productivity tools together.

- When I approached a similar situation, I found something really interesting in that intersection and with impact on both perspectives.

## We shouldn't put all things to do in the same place

Anybody who has tried Kanban realizes that as soon as you lock a specific task with a specific time/date, you are cooked. No one in modern manufacturing of physical or digital products uses time blocking for a reason.

But if you wake up in the morning and don't already know what you're doing that day, you're not working. You're on vacation.

The solution is to stop treating all to-dos as the same kind of thing. Appointments and meetings go into the calendar and are deducted from the time available to do things. Errands go on the fridge door, in a shared Reminders list, whatever lightweight tool works. And the real work — the things you need to produce — goes in a Kanban with columns that reflect the stages of your work, each with a WIP limit.

## We don't need to put all notes in the same place

There's no need to have a database of all your notes, interconnected. Everything isn't connected. The extra work of maintaining such a structure won't pay off, and the concept itself puts unnecessary pressure on your mind.

AI interactions actually make this clearer: tokens put a premium on context, which means you should only bring in what's relevant. That's a discipline worth having regardless of AI.

And with Claude Cowork, it doesn't matter if you have some stuff in Notion, some in a local folder, some in a repo. The agent bridges it.

## We didn't need an app

When I sat down to build my own custom productivity app with Claude Code, we arrived at a surprising conclusion: I didn't need one.

I didn't need to glue different productivity tools together because few of them were now needed, and there was no reason to connect content across different projects. And I didn't need an app — I just needed a place to keep the Kanban and make it accessible.

With Kanban, you're not planning when to do what. You're prioritizing in which order to do things, and re-prioritizing every time you sit down to work. You don't *push* work onto yourself for a certain time slot — you *pull* work from the Kanban when you have time. Deadlines just inform priority: if someone wants an article two weeks from now, you work backwards to figure out what card to pull today.

So instead of an app, I built an interactive HTML page that read from and wrote to a single .md file — no database needed. It displayed the data as a Kanban board and saved any drag-and-drop changes back to the file. Putting that file in an iCloud Drive folder made it available on my iPhone and iPad. Sharing the folder with Claude Cowork was the last step.

Cowork already had access to my calendar, so available time was accounted for — and I could sit down and do the *prioritization* together with Claude.

The 'app' became a) an .md file to hold the things I'm working on (each Kanban column is an H2, each card is a H3); b) the kanban.html to visualize it and to interact with drag-and-drop (it has also nice UI things like expand/collapse notes in the card); c) conversations with Claude Cowork about this content. 

And it was a bit uncanny how much Claude instantly 'knew'. Suggesting re-prioritizations based on the combo of things it saw. Insights I didn't immediately see. 

I can easily edit the .md file in iA Writer on my phone, and that's enough for updating the columns or adding something new. Those edits are then instantly updated on the Mac, since the file lives in the iCloud Drive folder. And when I work, I usually have my laptop so I don't need the full experience mobile. 

## The future isn't homegrown apps, it's HTML/CSS/JS + Claude

Based on this, I 

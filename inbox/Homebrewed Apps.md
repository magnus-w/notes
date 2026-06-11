# Home brewed apps and productivity

- As you wrote about in a Verge article, with Claude Code we can build our own custom apps.

- And in a previous Installer you told the inspiring story of how you built an app that glues Obsidian and other productivity tools together.

- When I approached a similar situation, I found something really interesting in that intersection and with impact on both perspectives.

## Summary

1. **Custom tools are feasible** — Claude Code enables building personal productivity apps tailored to individual workflows, as demonstrated by the author's experience.

2. **Separate to-do categories by type** — Different tasks belong in different places: calendar for appointments, lightweight tools (like Reminders) for errands, and Kanban boards for actual work with WIP limits.

3. **Don't centralize all notes** — Maintaining an interconnected database of everything is unnecessary overhead; instead, keep only relevant context accessible, which aligns with how AI agents work best with focused token usage.

4. **A simple HTML interface replaced a complex app** — The author discovered they didn't need a traditional app; instead, a single `.md` file + an interactive HTML Kanban visualizer solved the problem elegantly.

5. **Pull work instead of pushing it** — Rather than time-blocking tasks, prioritize work dynamically each session by pulling cards from the Kanban based on available time; deadlines inform priority rather than scheduling.

6. **The future is lightweight HTML/CSS/JS + Claude** — Simple, static-file-based tools paired with Claude's ability to understand context and suggest improvements offer a powerful alternative to traditional app development.

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

## The future isn't homegrown apps, it's vanilla HTML/CSS/JS + Claude

The future isn't homebrewed apps, it's vanilla web "apps" + Claude. 

Read your Verge article about homebrewed apps and got inspired. Also read the installer where you talked about the productivity tool you built and was in a similar situation. And was then surprised by what I found!

1. Looking at what to build, I realized that I didn't need all "tasks" in one place, or all notes in one place, interconnected. 
2. Since time blocking/time management has been proved as highly ineffective long ago (no manufacturer or software company uses it now), errands, meetings and appointments go in the calendar and nothing else. (What to buy for the kids school excursion needs nothing more sophisticated than the fridge door or a shared Reminders list.) 
3. The rest - what has to be done - goes obviously in a Kanban with more than three columns (reflecting whatever stages your process has) and WIP limits per column. 
4. Instead of **pushing** work on yourself (or others), i.e. by "planning" when it should be done, you **pull** the next, **highest priortized** item from the backlog column. Separate from working, and separate from adding new items, you prioritize and reprioritize the backlog items. 
5. Points 2-4 are nothing new, it's just basic Kanban and scientifically validated. But it's interesting how few seem to be using it when you read about their setups. The new thing - for me - was that applying this to a simlar mix of apps as yours (Obsidian, Todoist, Craft, etc.) had a surprisingly effective outcome:
6. a) A markdown file to hold the information; all the "cards" with tasks and, if needed, notes for each task. This way no database or external tool/service is needed. b)A HTML/CSS/JS Kanban.html that visulizes the data in the markdown file as a Kanban board. Dragging and dropping cards in across the columns in the browser, and editing/adding info on the cards, automatically updates the markdown file.
7. The markdown file lives in a folder in my iCloud Drive, so I can easily edit it from any device. And, crucially, Claude Cowork has access to the folder. 
8. Now I can run 'daily standups' and prioritizing 'meetings' with Claude Cowork and get its help with prioritizing tasks. And since it has access to my calendar and email, it already acts like a more advanced personal assistant than what Apple introduced with Siri AI day before yesterday. Specifically, much more context aware when it comes to details within my projects. 
9. I then took the next step and 'Claudified' my notes as well. So I no longer need Craft, Obsidian or similar. I have Notion for things where I need the ability to collaborate in a structured way with others, and since the both my Claude Code and Claude Cowork are connected to through the Notion MPC. 
10. The rest of my notes/files live in their respective 'projects folders'. When those are repositories, Claude Code automatically have access and knowledge. When they're not, I add them as contexts in Claude projects. Through Skills, Claude can read most document formats so I'm free to use any tool I need per respectice project. Instead of gaffa taping Craft, Obsidian or similar into doing things they aren't very good at for the sake of 'keeping things organized'.
11. Also, no need to find ways to connect differnt notes or files. Instead of 'knowledge management', backlinks and tags I just talk to Claude Cowork.

 # The future isn't homebrewed apps, it's vanilla web tech + Claude. 

> TL;DR - The core insight**: Stop forcing all tasks and notes into centralized systems. Instead, use proven principles (basic Kanban, pull-based work) with simple tools (markdown + HTML/CSS/JS) paired with Claude.

> **The stack**:
- **Markdown file** (in iCloud Drive) for all task/note data
- **HTML Kanban board** for visualization and drag-and-drop interaction
- **Claude Cowork** with access to your calendar, email, and files for intelligent prioritization and context-aware assistance

> **Key principles**:
- Separate concerns: Calendar for meetings, lightweight tools for errands, Kanban for actual work with WIP limits
- Pull work (from prioritized backlog), don't push it (time-block/time management)
- Distribute notes across project folders instead of maintaining one interconnected database

> **The result**: Replace fragmented tools (Obsidian, Todoist, Craft) with Claude + simple web tools. Claude bridges everything—reads your files, understands project context, acts as an advanced personal assistant for daily standups and prioritization. No database, no complex integrations, just accessible files and AI collaboration.

## The Big Drop
I read your Verge article about homebrewed apps and got inspired. Also read the installer where you talked about the productivity tool you built and was in a similar situation. And was then surprised by what I found!

1. Looking at what to build, I realized that I didn't need all "tasks" in one place, or all notes in one place, interconnected. 
2. Since time blocking/time management has been proved as highly ineffective long ago (no manufacturer or software company uses it), errands, meetings and appointments go in the calendar and nothing else. (What to buy for the kids school excursion needs nothing more sophisticated than the fridge door or a shared Reminders list.) 
3. The rest - what has to be done - goes obviously in a Kanban with more than three columns (reflecting whatever stages your process has) and WIP limits per column. 
4. Instead of **pushing** work on yourself (or others), i.e. by "planning" when it should be done, you **pull** the next, **highest priortized** item from the backlog column. Separate from working, and separate from adding new items, you prioritize and reprioritize the backlog items. In other words, after waking up you should never have to 'plan your day' because that's too late if you want to make it a productive one. You should already know what to do; Appointments in the calendar and then you just pull the next work item from the Kanban backlog.  
5. Points 2-4 are nothing new, it's just basic Kanban and scientifically validated. But it's interesting how few seem to be using it when you read about their setups. The new thing - for me - was that applying this to a simlar mix of apps as yours (Obsidian, Todoist, Craft, etc.) had a surprisingly effective outcome:
6. a) A markdown file to hold the information; all the "cards" with tasks and, if needed, notes for each task. This way no database or external tool/service is needed. b)A HTML/CSS/JS Kanban.html that visulizes the data in the markdown file as a Kanban board. Dragging and dropping cards in across the columns in the browser, and editing/adding info on the cards, automatically updates the markdown file.
7. The markdown file lives in a folder in my iCloud Drive, so I can easily edit it from any device. And, crucially, Claude Cowork has access to the folder. 
8. Now I can run 'daily standups' and prioritizing 'meetings' with Claude Cowork and get its help with prioritizing tasks. And since it has access to my calendar and email, it already acts like a more advanced personal assistant than what Apple introduced with Siri AI day before yesterday. Specifically, much more context aware when it comes to details within my projects. 
9. I then took the next step and 'Claudified' my notes as well. So I no longer need Craft, Obsidian or similar. I have Notion for things where I need the ability to collaborate in a structured way with others, and since the both my Claude Code and Claude Cowork are connected to through the Notion MPC. 
10. The rest of my notes/files live in their respective 'projects folders'. When those are repositories, Claude Code automatically have access and knowledge. When they're not, I add them as contexts in Claude projects. Through Skills, Claude can read most document formats so I'm free to use any tool I need per respectice project. Instead of gaffa taping Craft, Obsidian or similar into doing things they aren't very good at for the sake of 'keeping things organized'.
11. Also, no need to find ways to connect differnt notes or files. Instead of 'knowledge management', backlinks and tags I just talk to Claude Cowork.

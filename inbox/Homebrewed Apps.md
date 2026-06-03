# Home brewed apps and productivity

- As you wrote about in a Verge article, with Claude Code we can build our own custom apps.

- And in a previous Installer you told the inspiring story of how you built an app that glues Obsidian and other productivity tools together.

- When I approached a similar situation, I found something really interesting in that intersection and with impact on both perspectives.

## We shouldn't put all things to do in the same place

Anybody who has tried Kanban realizes that time management, time blocking and other calendar related approaches to planning reduces productivity by such an order of magnitude that no one in modern manufacturing of physical or digital products use it.

In other words, as soon as you lock a specific task with a specific time/date, you are cooked.

On the other hand, if you wake up in the morning and don't already know what you're doing that day, you're not working. You're on vacation. If you leave planning that late, you have neither efficiency, nor effectiveness.

In other words, appointments and meetings go into the calendar and are deducted from the time available to do things. 

Errands etc. go on the fridge door, in a shared Reminders list or whatever lightweight  tool that works. 

And the rest, the things we need to do, need to produce, go in a Kanban with more than three columns. Columns that reflect the stages of the kind of work you do. And columns that have a WIP limit.

## We don't need to put all notes in the same place

Strangely, the way AI interactions are structured now helps us think about work in way that would've been very valuable before as well. 

Like how tokens put a premium on context is something we should've mentally budgeted with before. There's no need to have a database of all your notes, interconnected. Because everything isn't connected. So the a) extra work of maintaining such a structure will not pay off. And the concept in itself will b) put an unnecessarily pressure on your mind. 

And now when we have Claude Cowork, it doesn't matter if you have some stuff in Notion (maybe because you want to collaborate with others on it) and some stuff in a local folder and some in a repo. 

## The agent is the app

This led to the interesting discovery that I didn't need a 'glue app' in two different senses: 

- I didn't need to glue together different 'productivity tools' because few of then were now needed and there was no need to connect content from different projects from each other.

- And I didn't need an app - I just needed a place to have the kanban and make it accessible to...wait for it!

As we've already seen, when you use Kanban, your are not  planning when to do what, you are prioritizing in which order to do things. And then you re-prioritize every time you sit down to work. You don't *push* work on yourself or for for a certain time slot, you *pull* work from the Kanban when you have time to work. 

What about deadlines and other 'outside hard dates'? You work backwards from them, defining what has to be done in order to meet that date and using this as the way to prioritize. 

(Is someone wants an article two weeks from now, you might need to have a pitch this week, an outline beginning next and the draft at the end of next week. So when you sit down this afternoon, you pull the 'Create article pitch' card from the Kanban because it's first in line.)

## Claude Code building for Claude Cowork

So when I sat down to build my custom app together with Claude Code, we collaboratively arrived at a surprising conclusion: 

We didn't need an app.

Instead I built an interactive html page that took all its data from a .md file (no need for a database), showed that data as a Kanban board and saved any changes made by drag and dropping the cards across columns or adding/editing text to that .md file. 

Placing that .md file in a folder on my iCloud Drive made it accessible on my iPhone and iPad and sharing the next step was sharing the folder with Claude Cowork. 

Cowork already had access to my calendar, so any meetings or appointments reducing available time was there and then I could sit down and do the *prioritization* together with Claude Cowork. 



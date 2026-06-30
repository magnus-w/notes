# Beta feedback - iPadOS 27

Root cause: Spotlight is the main heat source. corespotlightd has accumulated 946 hours of CPU time since June 4th — it's been stuck in a continuous re-index loop. spotlightknowledged.updater is currently peaking at 74.6% on top of that.

# Data_Verifications
I use Selenium Library in Python.
  ChromeDriver Version 95.0.4638.69.
Initially the site blocked access by selenium that in any access the site would not have raised the graph, I added options that simulate as close as possible to a normal person.
But sometimes the site does manage to detect the access as a robot so every time a block appeared I changed the ip
By a plugin I installed locally on my computer.
There are two types of apartments on the site that have a price history ,for sale, and apartments that have been sold.
The code knows how to deal with these two situations by checking whether it is sold or not and each of them has a different course of action in going over the graph.
In case of blockage by captcha a message will come out about it, and ip needs to be replaced

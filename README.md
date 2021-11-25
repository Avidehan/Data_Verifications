I use selenium to simulate a human transition on the price history graph \
• I  use Selenium Library in Python.\
• ChromeDriver version 95.0.4638.69.\
• Initially the site blocked access by selenium that in any access the site would not have raised the graph, I added options that simulate as close as possible to a normal person.\
• Sometimes the site does manage to identify the access as a robot, so every time a blockage appeared, I replaced the IP with a plugin that I installed locally on the computer.\
• There are two types of apartments on the site that have their price history, apartments for sale, and apartments sold.\
• The code knows how to deal with these two situations by checking whether it is sold or not and each of them has a different way of going through the graph.\
• In case of blockage by captcha, a message will be issued, and an ip must be replaced

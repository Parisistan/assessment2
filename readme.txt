This is my assessment

Assessment 2
Parisa
Full-stack 4

Question 1

1.1. a program is a specific set of ordered operations for a computer to perform. It was made as early as the 1940s. The computer gets one instruction and performs it and then gets the next instruction and it goes on. 

1.2. A process refers to an executing program in computer memory. In most operating systems, the execution of a process is in five different stages: start, ready, running, waiting, and termination. 

1.3. Cache is a memory system that temporarily stores frequently used instructions and data for processing for the CPU.

1.4. A thread is an execution context, and it is associated with a process and is used to give the process execution time on one of the computer systems processors. Threads are administrated by the operating system. Multithreading is a widespread programming and execution model that allows multiple threads to exist and be executed (however independently) within the context of one process.

1.5. Short for: global interpreter lock.
GIL is a mutual-exclusion lock held by a programming language interpreter thread. In Python, the GIL, protects access to Python code, preventing multiple threads from executing Python at once and prevents race conditions, ensuring thread safety.

1.6. Concurrency is the task of running and managing the multiple computations at the same time. VS. parallelism is the task of running multiple computations simultaneously. To understand this a bit better, we can say that concurrency is when two or more tasks can start, run, and complete in overlapping time periods. For example, multitasking on a single-core machine.  However, with Parallelism, tasks literally run at the same time.

1.7.
DRY: Don't Repeat Yourself
KISS: Keep it simple, Stupid
BDUF: Big Design Up Front, mostly used in waterfall method and not agile … where program's design has to be completed and perfected before that program's implementation is started e.g. banks.
1.8. The garbage collector is keeping track of all objects in memory. A new object starts its life in the first generation of the garbage collector. The way it works is that, Python periodically (based on last-time-used) frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.
1.9. A Livelock is a situation where a request for an exclusive lock is denied repeatedly, as many overlapping shared locks keep on interfering each other. The processes keep on changing their status, which further prevents them from completing the task. This further prevents them from completing the task. 
VS.
A deadlock is an unwanted situation where two or more transactions are waiting for one another to give up locks. For example, Transaction “A” might hold a lock on some rows in table-A and needs to update some rows in table-B to be able to finish. Deadlock is said to be one of the most feared complications in DBMS as it brings the whole system to a Halt. 
1.10. Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier. It is a useful framework for specially new developers since one can build a web application quickly using only a single Python file.

 
Question 2
Python 2 is an untyped language, and forces us to create new code. Python 3 improves the ease of writing and understanding code, as well as the performance of the code’s runtime. Python 3 is more in-demand and includes a typing system, while Python 2 is outdated and uses an older syntax for the print function. While Python 2 is still in use for configuration management in DevOps, Python 3 is the current standard. Python 2 uses ASCII—a method of encoding English characters with an assigned number, whereas Python 3 uses Unicode. This gives it the ability to represent non-English languages and no-Latin alphabets and other widely used symbols and emojis. 
 
 
Question 3
Refer to Palindrome Python file.
 
Question 4
Refer to Test_Palindrome Python file
 
Question 5
1. Daily Scrum = The Daily Scrum is a 15-minute time-boxed event for the Development Team to synchronise activities and create a plan for the next 24 hours. To reduce complexity, it is held at the same time and place every working day of the Sprint. If the Product Owner or Scrum Master are actively working on items in the Sprint Backlog, they participate as Developers.
2. Sprint Review = The Sprint Review is one of the most important ceremonies in Scrum where the team gathers to review completed work and determine whether additional changes are needed. It is mainly conducted to ‘Inspect’ and ‘Adapt’ the Product Backlog if required. The Scrum team and the stakeholders collaborate together during a Sprint Review and discuss what was done in the last Sprint and what more changes are required in the product. Based on this review, all the participants collaborate and decide on the things that could be done to get an optimized value and in what time-line.
3. Sprint Retro = The Sprint retrospective is a recurring meeting held at the end of a sprint used to discuss what went well during the previous sprint cycle and what can be improved for the next sprint. The Agile sprint retrospective is an essential part of the Scrum framework for developing, delivering, and managing. In retro, we talk about:  What went well? What can be improved? What didn't go so well? What have I learned?
 
Question 6
try:
	some code  — it allows you to run a block of code.
except:
	 allows you to handle errors from the try part (you can be specific with your type of error  and have more than one expcept e.g. ErrorValue or ErrorType
else: 
	allows you to execute code when there is no error.
finally: 
	always executes code no matters what and regardless of the result of the other parts
 
 
Question 7
We connect mySQL to Python from terminal and Pycharm terminal.
We first use a pip command to install mySQL in Pycharm terminal.
We should use our user and mySQL password (user is usually root and password is what we chose during mySQL setup).
We use the localhost or its IP that starts with 127. 
There are different methods for interacting with data from Pycharm. e.g. the cursor(), fetchmany() [to fetch many rows, we could also use fetchone()] or execute() 
We could use INSERT INTO to insert data and name.cursor()
 
 
Question 8
 
SELECT a.author_name
FROM authors a
JOIN books b
ON b.book_name = a.book_name
ORDER BY b.sold_copies DESC LIMIT 3;
 
Question 9
Refer to Python file



# **Statistics 30001 Instructor: Pieralberto Guarniero (Pier) Dept. Decision Sciences** 

**Material for students of course 30001 / Bocconi University. All Rights Reserved. Distribution - including via the web - without permission is prohibited.** 

## **Course Introduction: Objectives** 

The course introduces: 

 Techniques to properly **describe** and **summarize** different types of data, and to study their **relationships** 

 **Sampling** and **statistical inference** , with a focus on the potential **risks** associated to inference. The course assumes that students have a basic understanding of **probability** theory and **random variables** , which are covered in the course Mathematics Module 2 (Applied) - code 30063. 

The use of these tools in practice is illustrated through applications based both on **aggregated data** and on **datasets** . In the latter case, we will use the R statistical software and in particular the integrated development environment **RStudio** . Besides some basic functions, we will use the package **UBStats** developed exclusively for the course. The course heavily relies on the software, that will be also used during the exam. It is therefore essential to have both R and RStudio installed on your laptops both to attend the lessons and to take the exam. 

**2** 

## **Course Introduction: Lectures** 

## **The course is structured as follows:** 

- 28 lectures: introduction of the fundamental concepts of statistical data analysis and presentation of the main functions available in RStudio. 

 10 practical sessions (scheduled once per week): application of the techniques taught in the lectures by presenting problems to be solved either manually and/or using R tool.  Online meetings supporting students’ self -study; Q&A on exercises assigned on a weekly basis and on the application of the topics introduced during lectures and practical sessions. The schedule of the meetings will be posted on Bboard page common to all the classes **(30001 statistics - material exams)** 

## **Teaching materials** 

- Materials common to all the classes, reference slides, specific manual on the R software, summary exercises, mock exams, past exams, Q&A, available on the Bboard page common to all the classes ( **30001 statistics - material exams)** 

- WE HAVE A BOOK TAILORED TO THIS COURSE! 

**3** 

## **Course Introduction: Exams** 

**All the students can take the exam in two ways:** 

 2 midterms (1 hour; graded with 31/30 points maximum). Each midterm is passed with  a grade of 15 or higher. If both midterms are passed, the final grade is the average of the two achieved grades. To pass the overall exam, the final grade must be at least 18. 

- 1 general exam (2 hours; graded with 31/30 points maximum). The exam is passed with a grade of 18 or higher 

**All exams are closed book (you can use the R manual only) and involve** 

 Questions on theoretical aspects (definitions, proofs, properties of statistical tools) 

 Traditional exercises based on summaries of data (to solve manually - calculator or R)  Questions related to the analysis of data to be answered using Rstudio, which should be installed **on your laptop** before the exam (Please be sure that the software is properly set up and functioning ahead of time) 

Students attending at least the 75% of the lessons both in the first and in the second part of the course and who take the exam in **January or February** will get 1 point added to their final grade (Please note that such additional point does not contribute to the laude) 

**4** 

## **Workflow suggested by Pier** 

- Just **before class read the** (non annotated) **slides** to anticipate topics 

- Attend class! And during class try and be focused, engage and ask questions, make the – 

- most of your time which is super precious! 

- After class revise the annotated slides, write down doubts. Try and clarify them with your peers or ask me in the next lecture or via email. 

- Try and replicate the examples, exercises and scripts. 

- – 

- Attempt without looking at the solution first! the available exercises from our Bboard and from the common Bboard. 

**5** 

## **Main Resources for our specific adventure (Pier)** 

- Annotated slides (posted after each class) 

- Exercises sheets with solutions 

- Scripts from class (posted after each class) 

- R Videos 

- Past papers in the common BBoard 

- Solved exercises in the common BBoard 

**6** 

## **– Slides color coding specific to our class (Pier)** 

- **Blue slides** are fundamental concepts or information 

- **Red slides** are related to applications and R Studio 

- **Green slides** are **not** optional, but imo it’s enough to read through them. They might help your intuition. 

- are 

- **Gray slides optional.** They might be interesting in depth analysis, but you’ll survive without them. 

**7** 

# **STATISTICS: BASIC CONCEPTS** 

**Material for students of course 30001 / Bocconi University. All Rights Reserved. Distribution - including via the web - without permission is prohibited.** 

## **Decision making under uncertainty** 

In many cases it is necessary to make decisions, evaluate scenarios, define business strategies or political actions under uncertainty. 

- ' 

- ~~Identify the buying habits of a company s customers~~ 

- Determine the most effective marketing strategy for a certain target audience 

- Identify the most profitable customers 

- Select the candidates to admit to a master's program 

- Forecast the amount of orders for the coming year 

- Assessing the efficacy of a vaccine 

- Determine whether the average wages of men and women are different (gender pay gap) 

- stimating the rate of tax evasion 

In all these cases, proper statistical analysis of the data can support decision making. 

**9** 

## **Decision making under uncertainty** 

The statistical method encompasses all the necessary steps and procedures for processing and analyzing data to extract valuable and immediately applicable information, potentially aiding decision-making processes.  **Data collection and organization**  **Processing and analyzing data to describe and summarize their characteristics**  **Accurate and effective result description, communication and interpretation** 

 **Possible extrapolation from the obtained information, with a proper assessment of the associated risks** 

**10** 

## **Data collection and data preparation** 

A first, fundamental step is to define the required data concerning a specific problem, either by collecting new data or identifying existing information sources. 

**----- Start of picture text -----**<br>
Primary sources Secondary sources<br>Data collection Processing of primary sources<br>Observation Survey<br>Paper or electronic<br>format<br>Experiments<br>**----- End of picture text -----**<br>

**11** 

## **Population and sample** 

or a Data may refer to a **population sample** 

- **Population** (universe): the complete set of **all** units ( _**N**_ ) of interest in a study (all EU countries, all the citizens in a country, all the customers of a company,…). 

 **Sample** : _**subset of**_ the **population** . In some cases, collecting data on the entire population may be prohibitively expensive (high cost) or difficult or even impossible. For example, when the population is very large (set of all companies operating in Europe) or not fully accessible (difficulty in identifying all individuals in the population, e.g., all customers who purchased products of a certain brand); gathering data on the entire population becomes unfeasible. In such cases, it becomes necessary or convenient to collect data only on a portion of the population, which is represented _**n**_ by a sample ( ) 

**12** 

## **Random samples** 

~~To ensure the representativeness of the samples, it is essential to draw them~~ **randomly.** This way, the samples accurately reflect all units in the population and avoid biases towards specific groups of subjects 

**Simple random sampling** . The sample is selected in such a way that 

- Each unit is randomly and independently selected as a sample unit 

- Each unit of the population has an equal chance of 

   - being chosen 

- All the possible samples of the same size _**n**_ have the same chance of being chosen 

_**N**_ = 42 _**n**_ = 5 

There are more sophisticated sampling schemes and methods, that are not covered in the course. The focus will be on understanding and using simple random samples. 

**13** 

## **Key definitions: observations, variables and data** 

**Observation, case, or statistical unit:** entity (population unit) on which information is collected 

**Variable:** a characteristic of interest related to the cases under study 

**Data** observations made about the variable of interest measured on **(or measurements):** the cases under consideration 

**Values (or levels):** distinct values taken by the variable 

Data are commonly arranged in datasets, with **cases** listed in rows and **variables** represented in columns. 

**14** 

## **Datasets: examples** 

Ease of doing business: survey of the ease of doing business in different countries worldwide 

Information on **all countries globally** 

 **Cases:** the countries  **Variables** : indicators related to the ease of doing business in each country: 

 Starting or closing a business, paperwork requirements for building permits and property registration, labor regulation, access to credit, investor protection, taxation, trade, contract enforcement procedures... 

 **Data** : measurements on these indicators observed for each individual country 

**15** 

## **Datasets: examples** 

Collected data in the Ease of doing business survey (first 25 rows) 

**16** 

## **Datasets: examples** 

Loyalty cards and interviews 

Loyalty cards offer companies a wealth of information about customer characteristics and behaviors: 

 Upon subscription, data is collected, including gender, age, and area of residence. The loyalty card continues to provide valuable information, such as the number of visits, amount spent during a specific period, customer profitability (calculated based on spending, discounts, and marketing costs), and details of their most recent purchase. 

 Additionally, a specific targeted analysis can be carried out on a **random sample of** customers to gather information about their satisfaction levels regarding store features, value for money, and their propensity to recommend the service. 

**Cases:** the selected clients (the sample available for the analysis) **Variables:** information gathered from the loyalty card records and from interviews to clients **Data:** actual values on the variables measured on clients within the selected sample 

**17** 

## **Datasets: examples** 

Dataset (first 15 cases) created by merging information obtained directly from customers, data collected through loyalty card records, and data gathered through interviews conducted with a selected sample of customers 

The **values** of the surveyed variables have different **types** and characteristics! 

**18** 

## **Classification of variables** 

An initial classification of variables into **qualitative (categorical)** and **quantitative (numerical)** is based on the **type or nature** of the distinct values they take: 

- The values (or levels) of **qualitative** variables are **labels** indicating attributes, **group** membership, or identifying specific **categories** with distinct characteristics (gender, region of residence, level of satisfaction). 

- The values of **quantitative** variables are **numerical** 

**19** 

## **Classification of variables** 

Qualitative and quantitative variables can be further classified into subcategories based on their characteristics: 

## **Qualitative** variables: 

- **Nominal** (gender, business name of firms, region of residence): the variable’s values **cannot be ordered** . 

- **Ordinal** (satisfaction, level of education, positions in an organization chart, final ranking): ~~the variables~~ ’ ~~values can~~ ~~**be ordered** , but their differences cannot be quantified~~ 

- **Quantitative** variables: 

- **Discrete** data are generated by a **counting** process (number of children, number of visits to a store): the variable’s values are integers. 

- **Continue** data are a **measurement** of an generated by process (amount spent, height 

- individual, income): the values can take any real numerical value 

Note: In some cases, numerical variables may be **collected in classes** . For example, when surveying respondents' personal income, it might be difficult for them to accurately state the precise amount, so the data might be collected in income intervals or ranges. 

**20** 

## **Data Types/Variables** 

## **Variables** 

**Qualitative Quantitative Nominal Ordinal Discrete Continue** 

## **Examples: Examples:** 

- **Gender** • **Satisfaction levels** 

- • • **Payment methods Propensity to** 

- • **Region of residence recommend** 

• **Ranking Categories Categories Cannot be ordered Can be ordered** 

## **Examples:** 

**Examples: Examples:** • • **No. of purchased Amount spent products** • **Income** • **No. of children** • **Revenues Numbers Numbers Count Measurement** 

- **Amount spent** 

- • **Income** 

**21** 

## **Parameters and statistics** 

In general, we are interested to measure specific **characteristics of a set of data** . It is important to distinguish between: 

 **Parameter** : a measure that describes (or summarizes) a characteristic of the entire **population** . For example, we may be interested in assessing the proportion of Italian women who exit the labour market after the birth of their first child, or the proportion of European companies that registered a patent, or the average turnover of Italian companies operating in a certain industry. 

 **Statistic** : a measure that describes (or summarizes) a characteristic of a **sample** . For example, the proportion of respondents satisfied with a certain service, or the average number of purchase transactions within a specific period, or the average amount spent by the individuals in a sample. While our primary interest is the value of the **parameter for the entire population** , we must rely on the value calculated from the available sampled data. 

**22** 

## 

## **Descriptive statistics and inferential statistics** 

**Descriptive statistics** involves both graphical and numerical methods to summarize and or a . It analyze data. It can be applied to data from either the entire **population sample** includes a number of techniques for preparing, summarizing and effectively presenting data. 

## **Data presentation: Tables and graphs** 

**----- Start of picture text -----**<br>
2 5 0<br>2 0 0<br>15 0<br>10 0<br>5 0<br>2 0 3 0 4 0 5 0 6 0 7 0<br>**----- End of picture text -----**<br>

**Data analysis and synthesis: Summary measures, such as mean, variance, or correlation** 

**23** 

## **Descriptive statistics and inferential statistics** 

**Inferential statistics** involves methods used to make inferences and predictions about the population characteristics ( **parameters** ) based on information derived from sample data ( **statistics** ). 

A crucial issue of this process is to evaluate the **reliability** of such extension and the **risks** associated with using **sample** information to draw conclusions about the **entire** . **population** 

To accomplish this assessment, it is essential to take into account the **random mechanism** ( **probability** ) involved in the sample selection process, which leads to the inherent randomness in the fact that the available sample is just one of the many possible samples that could have been drawn from the population. 

**24** 

# **INTRODUCTION TO R & RSTUDIO (Handbook on the use of R)** 

**Material for students of course 30001 / Bocconi University. All Rights Reserved. Distribution - including via the web - without permission is prohibited.** 

## **R tool: structure** 

**R** is a programming language designed specifically for data manipulation, statistical analysis and graphical representation. 

It comes with an extensive collection of _**packages**_ (sets of functions) that come preinstalled with the basic version of R or can be accessed after installation. 

Data can be created from scratch in R, as well as imported from various sources (from hard disk or the web). 

The results of data processing (data, graphs, functions) can be printed, or saved as objects in R. These objects can then be further analyzed, manipulated, or saved on hard disks for future use. 

**RStudio** is an _integrated_ development environment (IDE)  for R. RStudio significantly simplifies the way users can interact with R and enhances the overall R programming experience. 

**26** 

## **Installation** 

## **To install R on your laptop, follow these instructions:** 

- Download from the R website (https://cran.r-project.org/) the executable file (.exe or .pkg) for the latest version of the R software for your operating system. For Windows, download from https://cran.r-project.org/bin/windows/base/ or for macOS download from https://cran.r-project.org/bin/macosx/base/) and run it. 

- Follow the installation instructions, accepting all default options. 

**To install Rstudio, follow these instructions (also available on Bboard).** 

- Download from the RStudio website (https://rstudio.com/products/rstudio/download/) the executable file (.exe or .pkg) for the latest version of **Rstudio Desktop** and run it. 

- Follow the installation instructions, accepting all default options. 

**27** 

## **Panes in RStudio** 

## When you start RStudio, three panes typically open: 

**Information about the R version being used Environment/History (this is the previous version) Console Files/Plots/Packages/ Help/Viewer** 

**28** 

## **Panes in RStudio** 

**Console** : execution pane. It is the interactive part of RStudio, where you can directly type and execute R commands. It allows you to interact with R in real-time and to see the results of your commands immediately. It reports submitted commands, provides information on the outcome of processing (reporting any errors), and, if required, displays the output. It is possible to work interactively and type commands directly into the console, but it is definitely better to collect them in a **script** 

**29** 

## **Panes in RStudio** 

**Environment/History:** In _**Environment**_ information is displayed on the R objects, variables, and data currently loaded into the R workspace during a session. 

_**History**_ keeps track of all R commands you have executed in the Console during a session, making it easy to recall and reuse previous commands. 

**30** 

## **Panes in RStudio** 

**Files/Plots/Packages/ Help/Viewer** : **multipurpose** pane showing the content of a directory on disk ( _**Files**_ ), any plots obtained during the session ( _**Plots**_ ), The loaded and available packages ( _**Packages**_ ; from this window it is also possible to install packages), and _**Help**_ pages regarding functions or packages (if required) 

**31** 

## **Panes in RStudio** 

## **from the** _**File**_ **Source** window. **Selecting NewFile|R Script menu opens the pane,** which can also be opened when opening ( **Open File** item on the _**File**_ menu) a previously saved R script 

In the **Source** pane you can write and edit R scripts. R scripts are a collection of commands written in the R programming language. To execute commands in the script, you must send them to the **Console** by selecting the portion of code to execute and pressing Enter or by clicking on the **Run** button or by placing the cursor at the end of a command and pressing Enter. 

**Scripts can be saved using the Save or Save as options on the** _**File**_ **menu.** 

**32** 


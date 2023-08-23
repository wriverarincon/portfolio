# Credit and Risk Analysis📊

## Overview
In this project, I worked with a dataset containing loan information, aiming to uncover valuable insights about shared attributes and traits among borrowers. As part of the same project, I designed a credit scoring mechanism, assigning individuals points based on specific attributes. Additionally, I formulated a risk assessment system, calculating a risk ratio for individuals using their unique attributes to determine potential risks of default.

## Key Features
1. **Data Cleaning:** I enhanced the dataset's suitability for analysis by performing various tasks, including eliminating null values, standardizing data formats for consistency, enhancing readability, and implementing filters to eliminate irrelevant data points.
2. **Exploratory Data Analysis:** I delved deeply into the dataset to conduct a comprehensive analysis, seeking valuable insights. By conducting EDA, I identified meaningful patterns, trends, and correlations within the data. These findings not only enhanced the overall analysis but also contributed to a more robust understanding of the dataset.
3. **Coding Techniques:** To develop novel mechanisms that enhanced the overall analysis, I employed coding techniques such as creating functions, utilizing list comprehensions, implementing conditional statements, and utilizing loops.
4. **Categorizing:** I grouped borrowers by assigning customized credit scores and risk ratios based on their attributes. This added an additional tool for uncovering correlations and insights within the data, thereby enhancing the final analysis.
5. **Outliers Detection:** I generated a variety of visual representations to offer clearer insights into the data's patterns and correlations, aiding in better understanding and analysis.

## Key findings from the Credit and Risk Analysis:
1. **Elevators of Credit Score:** A longer employment history, higher annual income, and an earlier opening date for the first credit line are all positively associated with higher credit scores.

2. **Credit Utilization:** A greater utilization of an individual's total credit limit corresponds to lower credit scores.

3. **Housing Status Influence:** Homeowners tend to have the highest credit scores, followed by those with mortgages, and finally, renters.

4. **Population Impact:** A higher state population exerts an influence on the total credit score; however, the average population does not exhibit the same effect.

5. **Factors of Risk:** Individuals with a larger number of open credit lines, an increased count of open credit card accounts, and a notable presence of installment accounts tend to display progressively higher levels of risk.

6. **Score vs. Risk Relationship:** The data indicates a negative correlation between credit scores and the risk of default. Nevertheless, even with elevated scores like 800 or 1000, some individuals maintain moderate to high levels of risk.

## Summary
### Within this extensive risk analysis, we have explored a diverse array of attributes, correlation patterns, default tendencies, and individual trends. By employing tailored models such as the "Credit Score" and "Risk of Default", we have devised an improved approach to categorizing subjects, facilitating a more precise examination of their attributes. These tools have yielded invaluable insights, enabling us to identify emerging trends that can aid institutions in pinpointing high-risk factors, including the number of credit lines or open credit cards. Indications of financial strain, such as a high volume of inquiries within a specified timeframe or credit utilization exceeding limits. Along with noteworthy attributes like employment duration, the inception of the first credit line, and annual income for potential borrowers. These findings collectively contribute to a more nuanced understanding of risk assessment and enhance an institution's ability to make informed decisions.

## Inquiries
## Inquiry: Are there specific attributes that remain consistent among individuals with high credit scores?
![image](https://github.com/wriverarincon/portfolio/assets/82168398/d31a1a58-1c6c-4072-b196-c43c8c940b2f)
#### In this collection of correlation charts, several patterns emerge:
#### 1- A clear positive correlation exists between employment length and credit score, as longer employment durations are associated with higher credit scores.

#### 2- Higher annual incomes are linked to elevated credit scores, indicating a direct relationship between income and creditworthiness.

#### 3- An intriguing finding is that individuals with high debt-to-income ratios can still achieve high credit scores. However, a closer examination reveals that the lowest the ratio, the higher the score tends to be. Most individuals in this dataset exhibit debt-to-income ratios below 40%, indicating a favorable distribution of financial stability.

#### 4- The earlier an individual established their credit line, the higher their credit score tends to be. Notably, those whose credit history dates back to 2000 or earlier are more likely to achieve the maximum credit score of 1000.

#### 5- Ownership status affects credit scores to some extent. Homeowners, particularly those who own their homes outright, tend to have higher credit scores than renters. The hierarchy of credit scores suggests that renters have the lowest, followed by mortgage holders, and then homeowners with full ownership.

#### 6- The data reveals a negative correlation between the limit-to-utilized ratio and credit scores. As this ratio increases, indicating higher credit utilization, credit scores generally decrease. However, it's worth noting that even when the ratio surpasses 50%, a significant portion of individuals maintain credit scores above 600. Furthermore, a few outliers have a limit-to-utilized ratio exceeding 100%, yet their credit scores remain relatively high at 600 or above.

## Inquiry: Which states rank among the top 10 for the highest credit scores, and could population size be a contributing factor?
![image](https://github.com/wriverarincon/portfolio/assets/82168398/581332ef-64e2-416d-8bd3-bd85350a5099)

#### Observing the data, it becomes evident that the leading states in terms of credit scores are the top 10, with California (CA) at the forefront boasting a total score surpassing 700,000. Texas (TX) follows closely with over 460,000, and New York (NY) and Florida (FL) trail in the third and fourth positions, amassing nearly 400,000. The subsequent chart provides insights into the average credit scores of these states, which consistently hover around 700. Among these, New York records the lowest average around 670, while Georgia (GA) takes the lead with an average exceeding 710. Furthermore, the third chart showcases the total state population by 2015, revealing a noteworthy correlation with the prior analyses. It is evident that higher population states tend to exhibit higher total and average credit scores, aligning with our expectations.

## Inquiry: Is it possible to forecast the likelihood of a borrower defaulting on their loan by analyzing their financial attributes?
#### We're going to develop a model akin to the previous credit scoring approach. However, in this iteration, we'll adopt a percentage-based methodology. We'll follow a similar framework of awarding points based on specific criteria derived from a range of columns. This approach will aid us in assessing the probability of an individual's likelihood to default.
![image](https://github.com/wriverarincon/portfolio/assets/82168398/e0e3e866-46ab-426d-afc4-f5bae9c46009)
#### Based on our chart, it becomes evident that 75% of the dataset presents risk percentages below 40%. This distribution highlights a prevalent occurrence of risk percentages ranging from 20 to 40, signifying a categorization into the low to medium risk range. Additionally, a noticeable skew towards the higher end is observable, with the maximum threshold nearing 70% and an exceptional outlier surpassing 80%. Further exploration is needed to gain deeper insights into these noteworthy values.

## Inquiry: Do high-risk borrowers share any consistent attributes?
![image](https://github.com/wriverarincon/portfolio/assets/82168398/86a2c806-8801-400a-b914-e8de8922d160)
#### The data unmistakably reveals a conspicuous pattern emerging from the correlation charts. The trends underscored within these visual representations suggest a clear tendency: individuals possessing a larger number of open credit lines, elevated counts of open credit card accounts, and a notable presence of installment accounts tend to display a distinct and gradually intensifying degree of risk.

#### A compelling observation arising from the data is that even individuals with a high percentage of accounts consistently maintaining a delinquency-free status tend to align with a moderate risk of default.

#### On the other hand, attributes such as the count of delinquencies within the last two years or the number of inquiries in the preceding two months do not exhibit a significant correlation with higher default risk. Funny enough, those with lower count of inquiries or deliquencies are the ones with medium risk of default.

## Inquiry: Does a correlation exist between potential default and the assigned credit scores?
![image](https://github.com/wriverarincon/portfolio/assets/82168398/b4d4dd35-71d2-4331-b9b8-fa6933520f2b)
#### The majority of the data points exhibit credit scores surpassing 600 and fall within the range of 20% to 30%. The distribution pattern indicates a noteworthy trend: as the credit score escalates, the associated risk diminishes. However, it's noteworthy to highlight that even at elevated scores such as 800 or even 1000, there remain individuals with moderate to high levels of risk.

#### Examining the chart's left segment, which encompasses the region below the 10% risk threshold, it becomes apparent that within this limited subset, higher credit scores (600 and above) predominate. Conversely, the right-hand corner of the chart reveals an interesting contrast: above the 50% risk mark (indicative of high risk), there exists a slightly larger population compared to the opposing side, despite both segments maintaining a prevalence of high credit scores.

Your feedback and suggestions are highly appreciated! Let's embark on this financial journey together. 💰🚀

## License

This project is licensed under the [MIT License](LICENSE).

---


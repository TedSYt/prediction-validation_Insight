# prediction-validation_Insight


# approach
My code has  4 sections: 
First, read the pipe-delimited data from the txt files by pandas. In order to process large amounts of data, a '''chunksize''' of 1000 is applied for pandas to read the data.

Second, extract the key information from the raw data. This include the time-period of the stock's price, i.e. the longest hour appear in the data. The data is stored appropriatly in different data type. For example, the '''window''' used for iterator and index is stored as intger.

Third, calculate the '''average error''' with the help of '''error'''. This part will first calculate the '''error''' between the predicted and the actual data in the same time period(with the minmium length 1 hour). At the same time, the number of the stocks which exists in both the 2 files at the same time period is remembered. Finally, with the integer '''window''', we can use the '''error''' and the chart of '''number of stocks''' to calculate the '''average error'''.

Finally, out put the result and write it in the txt file. In this part, I print the result in a txt files with the '''average error''' being rounded off to 2 decimal places. A .txt is created in the output folder and the .sh will open the whole Python file to let all the steps work.

# dependencies
In the projects, I used pandas and numpy to process my data and do the calculation. Thanks for the resources on google for me to deal with so many minor problems of my code!

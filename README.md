# tip_dir

This repository stores the python, and other code for cleaning the data from my pizza delivery log. 

This data was recorded in 4 fields. 

The date, the shift (beginning hour and end hour), the number of deliveries taken, and the dollars taken home in tips. 

The project expands on this information and draws out additional points. 

From the date, using Excel, it expands on the day of the week for every row. 

For the shift, parsed also in Excel, this information is parsed out to contain the starting time and the end time, as well at the difference, which is the length of the shift. 

Addtionally, a boolean variable is included, whether the shift is a Day shift or an Evening shift (given as beginning before 2 PM or after).

Finally, a series of columns are given that stand for individual clock hours, from '0' to '23', where '0' is midnight. 
For each row, each clock column is entered as 1 if it is contained within the shift for that row, and 0 if not. 
The final hour number is not included. (If the shift ends at 4, then the 4 oclock hour is not included).


All of these points are used for study in some way, which have all been derived from 4 intitial fields.


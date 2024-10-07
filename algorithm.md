# Algorithm Document

1. Output program explanation to user
2. Ask user to input total data used in month, assign value to total_gb
2. Ask user to input their color package
3. Set input to lowercase 
3. while color package is not blue, green or purple, 
   1.ask user to input color package again.
   4. set input to lowercase
3. If user enters green:
   5. If total_gb used in month is greater than 2:
      6. Subtract 2 from total_gb, then multiply by 15.00 and add 49.99
   8. Else:
      9. Monthly_fee = 49.99
   10. Ask user if they have a coupon
       11. If user has a coupon:
           12. If user total >= 75.00:
               13. subtract 20.00 from total.
           14. Else:
               15. Total remains unchanged.
16. If user enters Blue:
    17. If total_gb used in month is greater than 4:
        19. Subtract 4 from total_gb, then multiply by 10.00 and add 70.00
    20. Else:
        21. total remains 70.00
22. If user enters purple:
    23. Total = 99.95
24. Output total monthly fee, output total_gb
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid_value  
            
        elif mid_value < target:
            left = mid + 1
            
        else:
            right = mid - 1

    return None


# # # 2. Skapa en loop som läser in sökord rad för rad
# while True:
#     try:
#         target = input().strip()
        
#         # Om vi hittar '#', avbryt loopen (programmet är klart)
#         if target == '#':
#             break
            
#         # Använd din sökfunktion och skriv ut vad den returnerar
#         resultat = binary_search(sorted_list, target)
#         print(resultat)
        
#     except EOFError:
#         # Fångar upp om testsystemet oväntat slutar skicka data
#         break
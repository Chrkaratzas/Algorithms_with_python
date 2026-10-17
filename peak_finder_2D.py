import random

# 1. Ορισμός διαστάσεων του πίνακα (Γραμμές x Στήλες)
rows = 5
cols = 6

# Δημιουργία 2D πίνακα με τυχαίους ακέραιους αριθμούς (π.χ. από 1 έως 99) με randint
A = [[random.randint(1, 99) for _ in range(cols)] for _ in range(rows)]

# Εκτύπωση του αρχικού τυχαίου πίνακα για να βλέπουμε τα νούμερα
print("Ο τυχαίος πίνακας που δημιουργήθηκε:")
for r in A:
    print(r)
print("-" * 40)

# 2. Αρχικοποίηση μεταβλητών για τη δυαδική αναζήτηση
left = 0
right = cols - 1
found_peak = None

# ΟΣΟ left <= right ΕΠΑΝΑΛΑΒΕ
while left <= right:
    mid = (left + right) // 2  # DIV 2
    
    # i_max <- γραμμή με τη μέγιστη τιμή στη στήλη mid
    i_max = 0
    for row in range(1, rows):
        if A[row][mid] > A[i_max][mid]:
            i_max = row
            
    # Ασφαλής έλεγχος ορίων (Boundary Checks) για τις στήλες mid-1 και mid+1
    is_greater_than_left = (mid == 0) or (A[i_max][mid] >= A[i_max][mid - 1])
    is_greater_than_right = (mid == cols - 1) or (A[i_max][mid] >= A[i_max][mid + 1])
    
    # ΑΝ A([i_max],[mid]) >= A([i_max],[mid - 1]) και A([i_max],[mid]) >= A([i_max],[mid + 1]) ΤΟΤΕ
    if is_greater_than_left and is_greater_than_right:
        found_peak = (i_max, mid)
        break  # Έξοδος από το while αφού βρέθηκε η κορυφή
        
    # ΑΛΛΙΩΣ ΑΝ A([i_max],[mid - 1]) > A([i_max],[mid]) ΤΟΤΕ
    elif mid > 0 and A[i_max][mid - 1] > A[i_max][mid]:
        right = mid - 1
        
    # ΑΛΛΙΩΣ
    else:
        left = mid + 1

# 3. Εκτύπωση του αποτελέσματος
if found_peak is not None:
    i_res, j_res = found_peak
    print(f"Η κορυφή βρέθηκε στη Γραμμή {i_res}, Στήλη {j_res}")
    print(f"Η τιμή της κορυφής είναι: {A[i_res][j_res]}")
else:
    print("Δεν βρέθηκε κορυφή.")

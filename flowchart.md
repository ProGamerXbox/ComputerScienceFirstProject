```mermaid
graph LR
A[Start] --> B[Initialize hangman_list, alphabet]
B --> C[Define start function]
C --> D[Choose a random word from hangman_list]
D --> E[Get word length]
E --> F[Initialize tries, wrong_guessed_word, hintguesses]
F --> G[Print initial hintguesses]
G --> H[Print hangman ASCII art]
H --> I[Print word length]
I --> J[Get user input for letter guess]
J --> K[Check if letter guess is valid]
K --> L[Check if letter has been guessed before]
L --> M[Check if letter is in the word]
M --> N[Print hangman ASCII art]
N --> O[Print letter is in the word message]
O --> P[Update hintguesses with correct letter guess]
P --> Q[Print updated hintguesses]
Q --> J
L --> R[Add letter to wrong_guessed_word]
R --> N
M --> S[Increment tries]
S --> T[Check if maximum tries reached]
T --> U[Print hangman ASCII art]
U --> V[Print game over message]
V --> W[Print the correct word]
W --> X[Ask user for replay choice]
X --> Y[Check replay choice]
Y --> Z[Restart game]
Z --> J
Y --> AA[Exit the script]
AA --> AB[End]
T --> AB
```
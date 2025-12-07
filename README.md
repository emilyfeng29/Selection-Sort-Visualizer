# Selection-Sort-Visualizer
## Algorithm Name 
Selection Sort Visualizer
## Screenshot of test 
incorrect answer:
<img width="1534" height="782" alt="Screenshot 2025-12-06 194017" src="https://github.com/user-attachments/assets/bb1bda27-ff86-4771-a342-96faf32a01d2" />
correct answer:
<img width="1537" height="785" alt="Screenshot 2025-12-06 194930" src="https://github.com/user-attachments/assets/e261e439-7756-494e-af9b-13116aa47cee" />
no input:
<img width="1526" height="688" alt="Screenshot 2025-12-06 195110" src="https://github.com/user-attachments/assets/99fdfeff-f09d-4c70-935b-1bf903edc118" />
invalid input:
<img width="1526" height="687" alt="Screenshot 2025-12-06 195222" src="https://github.com/user-attachments/assets/f9cb0b57-a05f-4d1a-9908-91f5e1289c8c" />


## Problem Breakdown & Computational Thinking 
I chose Selection Sort because it is simple and easy to understand, and it sorts the list in-place without using extra memory. Its predictable process of finding the minimum element makes it ideal for small datasets and for demonstrating sorting concepts. Compared to search algorithms, sorting the data first helps make later searches or analyses clearer and more organized.

Decomposition 
- Generate a random list of integers
- Let the user input their sorted list
- Check correctness
- Play a sound for success or failure
- Visualize the selection sort step-by-step (show swaps and new minimums)

Pattern recognition 
- Finds the minimum in the unsorted part of the list
- Swaps it with the first unsorted element
- Moves the boundary between sorted and unsorted sublists

Abstraction
- Track current index and minimum
- Steps of the array state, check if user input is correct

Algorithmic thinking
- The user inputs their sorted list, which then flows through the code and produces a result based on their input.
- The input is then sent to the processing function, where the Selection Sort algorithm organizes the numbers in ascending order
- Once the sorting is complete, the output is returned to the GUI, displaying the sorted list in a separate text box.

Flowchart:

<img width="438" height="655" alt="Screenshot 2025-12-05 175037" src="https://github.com/user-attachments/assets/161b2572-d443-4191-b373-980c1fff4135" />

## Steps to Run 
- Step 1: Click **Generate List**
- Step 2: Enter your sorted list
- Step 3: Click **Run Selection Sort**

## Hugging Face Link 
https://huggingface.co/spaces/emilyfeng29/selection-sort-visualizer

## Author & Acknowledgment
AI was used to teach how to add audio

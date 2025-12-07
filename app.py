from google.colab import files

# Upload sound files
correct_sound = files.upload()
incorrect_sound = files.upload()

import random
import gradio as gr

# max number of steps to show on the GUI
max_steps = 10

# generate a random list
def generate_list():
    arr = random.sample(range(1, 30), 8)
    display = f"Random unsorted list:\n {arr}"
    return display, arr

# run selection sort step by step
def selection_sort(arr_state):

    # if user doesn't generate a list
    if not arr_state:
        list_msg = "Click 'Generate List' first"
        return (
            list_msg,
            # step explanation boxes
            *["" for _ in range(max_steps)], 
            # state boxes
            *["" for _ in range(max_steps)],
            # final message
            "No list to sort."
        )

    # copy of array so the orginal list doesn't change
    arr = arr_state[:]
    # stores text explaining each step
    steps = []
    # stores the list stae after each iteration
    states = []

    # selection sort
    n = len(arr)
    i = 0

    while i < n - 1:
        min_idx = i

        # explains what index we are checking
        states.append(f"Assume index {i} (value {arr[i]}) is minimum")

        # finds the smallest element value in the unsorted list
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # shows where the new minimum value is
        steps.append(f"New minimum at index {min_idx} (value {arr[min_idx]})")

        # swap if minimum is not alreadt at position i
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            #show updated list
            states.append(f"{arr}")
        else:
            # no change happened
            states.append(f"{arr}  (no swap)")

        i += 1

        # stop if it exceeds the max steps to show on the GUI
        if len(steps) >= max_steps or len(states) >= max_steps:
            break

    # pad UI boxes
    while len(steps) < max_steps:
        steps.append("")
    while len(states) < max_steps:
        states.append("")

    # output messages
    final_msg = f"Sorted list:\n {arr}"
    list_display = f"Random unsorted list:\n {arr_state}"

    # returns everything
    return list_display, *steps[:max_steps], *states[:max_steps], final_msg

# Check user input and play audio
def check_user_input(user_input, arr_state):

    # check if the list exists
    if not arr_state:
        return "Click 'Generate List' first", None

    # checks if the user input box is empty
    if not user_input.strip():
        return "Please enter a comma-separated list", None

    # convert input into a list of integers
    try:
        user_list = [int(x) for x in user_input.split(',')]
    except ValueError:
        return "Invalid input. Please enter a comma-separated list of integers.", None

    # compare user's list to the correct list
    if user_list == sorted(arr_state):
        return "Correct!", "correct.mp3"
    else:
        return "Incorrect. Try again!", "incorrect.mp3"

# UI
with gr.Blocks(title="Selection Sort Visualizer", css = """
body {
    background-color: #FFFFFF;
}
.gradio-container {
    border-radius: 20px;
    background-color: #FFFFFF;
}
button, .gr-button {
    background: #E2EAF4 !important;
    color: black !important;
    border-radius: 10px !important;
}

label {
    font-weight: bold !important; colour: #E2EAF4;
}
""") as demo:

    # title and explanation
    gr.Markdown("""
        # Selection Sort Visualizer
        ## How Selection Sort Works

        Selection Sort is a simple comparison-based sorting algorithm.
        It sorts a list **by repeatedly selecting the smallest remaining value** and swapping it into the correct position.

        ### Step-by-step:
        1. Look at the current position `i` in the list.
        2. Search the **rest of the list** to find the **smallest value**.
        3. If a smaller value is found, **swap** it with the value at position `i`.
        4. Move to the next position and repeat until the list is sorted.

        **Key idea:**
        Each pass finds the smallest item in the *unsorted* part of the list and places it in the *sorted* part.
        """)

    gr.Image("https://tse3.mm.bing.net/th/id/OIP.FRSNBACr3kiYDVdvpyaQ_gHaEn?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", label = "Selection Sort Example")

    # instructions
    gr.Markdown("""
        ## Generate a Random List
        Click the button below to start!
        **Step 1:** Click **Generate List**
        **Step 2:** Enter your sorted list**
        **Step 3:** Click **Run Selection Sort**

    """)

    # stores the list for all functions
    arr_state = gr.State([])

    # button to generate a random list
    with gr.Row():
        generate_button = gr.Button("Generate List", variant="secondary")

    # displays the list
    list_box = gr.Textbox(label="Generated List", lines=2, interactive=False)

    # user enters their sorted list
    gr.Markdown("Test Yourself — Enter Your Sorted List")
    user_sorted_input = gr.Textbox(
        label="Enter your sorted list (comma-separated)",
        placeholder="e.g., 2, 5, 10, 13, 22 ..."
    )

    # button to run 'check my answer'
    check_button = gr.Button("Check My Answer")
    check_output = gr.Textbox(label="Check Result", interactive=False)
    audio_feedback = gr.Audio(label="Audio Feedback", interactive=False)

    # button to run 'run selection sort step-by-step'
    run_button = gr.Button("Run Selection Sort Step by Step", variant="primary")

    # step-by-step search explanation
    gr.Markdown("Search Steps")
    step_boxes = [gr.Textbox(label=f"Step {i+1}", lines=1, interactive=False) for i in range(max_steps)]

    # shows the array after each iteration
    gr.Markdown("Array State After Each Iteration")
    state_boxes = [gr.Textbox(label=f"Array {i+1}", lines=1, interactive=False) for i in range(max_steps)]

    # displays the final sorted list
    result_box = gr.Textbox(label="Result", lines=2, interactive=False)

    # button callbacks

    # updates list_box and arr_state after 'generate list' button is clicked
    generate_button.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_box, arr_state]
    )

    # fills step boxes and final result after 'run selection sort' button is clicked
    run_button.click(
        fn=selection_sort,
        inputs=arr_state,
        outputs=[list_box, *step_boxes, *state_boxes, result_box]
    )

    # displays message and audio after 'check my answer' button is clicked
    check_button.click(
        fn=check_user_input,
        inputs=[user_sorted_input, arr_state],
        outputs=[check_output, audio_feedback]
    )

# runs the GUI
demo.launch()

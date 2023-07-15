## Algorithm Visualizer - pygame
I created this project to learn `pygame` and I wanted to create a Sorting Algorithm Visualizer from a long time.

### Functions
1. Menu to select Different Sorting Algorithms
2. `Play` & `Pause` button to control the Visualization
3. `Reset` Button to reset the data on the screen
4. Each Algorithm has different visualization; the explanation of each visualization can be found on my website [colilhasnel.com](https://www.colilhasnel.com/)

### Requirements
- You can run the command `pip install requirements.txt` in powershell. 
- The requirements are :
    - python3
    - pygame

### How to play
- Run the `visualizer.py` as a python file

### Adding new Algorithms
1. Add a `select_algorithm_button` object in `Visualizer.py/algorithms_menu` function
    - The format should be is `algorithm_buttons["Algorithm_name"] = select_algorithm_button( algorithm_number, "Algorithm_Name", display_algorithm.algorithm_function)`
    - algorithm_number = Decides the position of button on the Menu Screen, Each algorithm has a unique algorithm_number
    - "Algorithm Name" = This is what you think it is. It should be a string
    - display_algorithm.algorithm_function = This points to the actual visualization function in `display_algorithm.py` file
2. Add a `algorithm_funciton` in `display_algorithm.py` file
    - This should be a `<generator>` function. Read on more on [generator functions and objects here](https://www.geeksforgeeks.org/generators-in-python/)
    - You should code the entire algorithm in this funciton
    - Update `global_info.color` array whenever you the algorithm performs a swap
        - Use your own creative to make better visualizations
    - Add `global_info.draw_data(j)` to update that particular as per the color defined
        - If no `j` argument is passed, `global_info.draw_data()` will update the entire **Data**
    - add `yield` at appropriate places for `Pause` function to work
    - Refer `bubble_sort` function to understand how to add visualization on iterative algorithms
    - Refer `quick_sort` function to understand how to add visualization on recursive algorithms
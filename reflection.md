# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, the interface loaded, but the gameplay logic was inconsistent. First, the hint direction was wrong: when the secret number was 75 and I guessed 70, the game said “Go LOWER!” even though it should have said “Go HIGHER!”. Second, the attempt tracking did not match between the main display and the debug panel, since one part showed 7 attempts left while another already showed 1 attempt used. Third, the same guess appeared to be processed more than once, causing duplicate history entries and inconsistent submit behavior.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used an AI assistant in VS Code to help understand the logic behind the bugs I observed while running the game. I provided the AI with context from the project files, especially app.py and logic_utils.py, so it could analyze the gameplay logic.

One correct suggestion from the AI was identifying that the hint logic was reversed. When the secret number was higher than my guess, the game sometimes displayed the wrong hint direction. The AI explained that the comparison logic between the guess and secret number might be flipped, which I confirmed by reviewing the code.

The AI also suggested improvements such as refactoring logic into logic_utils.py and adding more tests for edge cases like invalid inputs. However, one suggestion that was less helpful was focusing on structural refactoring before fixing the gameplay logic itself, so I verified the behavior by manually running the game multiple times to confirm the actual bugs.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed only after I verified it in both the running streamlit app and the test suite. For the hint bug, I manually tested guesses above and below the secret number and checked that the game showed “Go HIGHER!” when the guess was too low and “Go LOWER!” when the guess was too high. For the attempts bug, I compared the “Attempts left” message in the UI with the “Attempts” value in the Developer Debug panel to make sure they matched the configured attempt limit.

One test I ran was pytest -q, which showed that all three tests passed after my changes. I also manually tested the game by entering several guesses and watching the secret number, attempts, and hint messages in the debug panel. This showed me that the hint logic was now correct and that the attempts counter was behaving consistently.

AI helped me understand what to test by pointing out the lines that were causing the reversed hint behavior and the off-by-one attempt issue. It also suggested that I verify the fixes by testing concrete examples in the app instead of only trusting the code changes. That made it easier to confirm that the bugs were actually fixed in gameplay.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time the user interacts with the app, such as clicking a button or entering input. Because of this, variables would normally reset on each interaction. Streamlit’s session_state allows the app to store values like the secret number, attempts, and score so they persist across reruns. This project helped me understand how session_state is important for maintaining game state and ensuring that user actions update the interface correctly without losing previous values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is testing changes step by step instead of assuming a fix works. In this project I ran the app repeatedly and used the debug panel to verify the secret number, attempts, and history to confirm whether the logic behaved correctly.

Next time I work with AI-generated code, I would more carefully review the logic before trusting it. AI-generated code can look correct but still contain subtle bugs, so it is important to read the code and test edge cases.

This project showed me that AI-generated code can be useful for building a starting point, but developers still need to carefully debug and verify the behavior of the program.
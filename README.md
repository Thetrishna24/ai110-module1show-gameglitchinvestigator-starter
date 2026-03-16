# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The purpose of this game is to let a player guess a secret number within a limited number of attempts. The game provides hints such as "Go HIGHER!" or "Go LOWER!" to guide the player toward the correct number. The game also tracks attempts, score, and guess history using Streamlit session state.

While testing the AI-generated code, I found that the hint logic was incorrect. When the secret number was larger than the guess, the game told the player to go lower instead of higher. This happened because the secret number was converted to a string before being compared with the guess, which triggered a fallback comparison and reversed the hint logic. I also noticed inconsistencies in how attempts were tracked between the UI and the debug panel.

To fix these issues, I ensured that the secret number is always treated as an integer when passed to the `check_guess()` function. This prevents the fallback comparison logic from reversing the hints. I also verified that attempts start at zero and increase only when a guess is submitted so the attempts counter matches the number of guesses made. After these changes, the hints display correctly and the attempts counter behaves consistently.

## 📸 Demo

- [ ] [ai110-module1show-gameglitchinvestigator-starter/ss1.png]
- [ ] [ai110-module1show-gameglitchinvestigator-starter/ss2.png]
- [ ] [ai110-module1show-gameglitchinvestigator-starter/ss3.png]
- [ ] [ai110-module1show-gameglitchinvestigator-starter/ss4.png]
- [ ] [ai110-module1show-gameglitchinvestigator-starter/ss5.png]
  

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

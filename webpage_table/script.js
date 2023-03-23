// obtain references to the visible rows' question text
const questions = document.querySelectorAll('th.question');
// obtain references to all rows (visible and invisible)
const allrows = document.querySelectorAll('tbody tr');

// hidden content
const answers = ['purple', 'банитса (banitsa)'];
const CHILDNUM = 0;

// register event listeners to each visible question, for the hidden row below it
const clickCounts = Array(questions.length).fill(0);

for(let i=0; i < questions.length; i++) {
    questions[i].addEventListener(
        "click",
        () => {
            togglerow = allrows[i*2 + 1];
            togglerowtext = togglerow.children[CHILDNUM].innerText;

            // populate content onto page the first time the question is clicked
            // (not sure why, but it wasn't updating using togglerowtext, had to re-access the innerText)
            if (togglerowtext === "")
                togglerow.children[CHILDNUM].innerText = answers[i];

            // toggle visibility
            if (clickCounts[i] % 2 === 0)
                togglerow.classList.remove("hidden");
            else
                togglerow.classList.add("hidden");
            clickCounts[i] += 1;
        }
    );
}
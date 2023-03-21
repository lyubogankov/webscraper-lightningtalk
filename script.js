const descriptions = document.querySelectorAll('td.description')
const allrows = document.querySelectorAll('tbody tr')

// register event listeners to each description, for the row below it

const clickCounts = Array(descriptions.length).fill(0);

for(let i=0; i < descriptions.length; i++) {
    descriptions[i].addEventListener(
        "click",
        () => {
            if (clickCounts[i] % 2 === 0)
                allrows[i*2 + 1].classList.remove("hidden");
            else
                allrows[i*2 + 1].classList.add("hidden");
            clickCounts[i] += 1;
        }
    );
}
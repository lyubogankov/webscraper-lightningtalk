// obtain references to the visible rows' description text
const descriptions = document.querySelectorAll('td.description')
// obtain references to all rows (visible and invisible)
const allrows = document.querySelectorAll('tbody tr')

// hidden content
const payment_methods = ['Online', 'Online', 'Online', 'In-person', 'In-person', 'In-person', 'In-person'];

// register event listeners to each visible description, for the hidden row below it
const clickCounts = Array(descriptions.length).fill(0);

for(let i=0; i < descriptions.length; i++) {
    descriptions[i].addEventListener(
        "click",
        () => {
            togglerow = allrows[i*2 + 1];
            togglerowtext = togglerow.children[1].innerText;

            // populate content onto page the first time the description is clicked
            // (not sure why, but it wasn't updating using togglerowtext, had to re-access the innerText)
            if (togglerowtext === "")
                togglerow.children[1].innerText = payment_methods[i];

            // toggle visibility
            if (clickCounts[i] % 2 === 0)
                togglerow.classList.remove("hidden");
            else
                togglerow.classList.add("hidden");
            clickCounts[i] += 1;
        }
    );
}
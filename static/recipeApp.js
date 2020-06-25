"use strict";


$('.recipe_card').on('click', (evt) => {
	evt.preventDefault();

	let recipe_id = evt.currentTarget.name
	
	// console.log(evt)
	// console.log(evt.currentTarget.name)
	// console.log(evt.currentTarget.innerHTML)
		
	$.post('/user_fave', {'recipe_id':recipe_id}, (response) =>{
		
		// if response at status = ok then:
		evt.currentTarget.innerHTML = "Liked!"
		// otherwise print "You've already liked this one"
	});
});



const filter = document.getElementById('ingredient_filter');
const recipe_cards = document.querySelectorAll('.card');
// ^ a list of notes


filter.addEventListener("keyup", (evt) => {
	evt.preventDefault();
	if (evt.keyCode === 13) {
		filter.click();
		
		let ingredient = console.log(filter.value);
		
		for (const recipe of recipe_cards){
			let text = recipe.textContent
			if (text.includes(ingredient))
			// if ingredient in text:
					// make div disappear from screen

		}


	}

	
});


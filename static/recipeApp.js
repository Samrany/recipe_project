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
	}

		let ingredient = console.log(filter.value);

		// for loop over recipe_cards and search if ingredient is in text.
		// 	if yes, remove from screen



		// select all divs that don't contain string and disappear
		// let filter.placeholder = ingredient_name;
		// let filter.placeholder = " ";
		// console.log(ingredient_name)
		// console.log("event listener worked")
		// console.log(filter)

	
	
	// {
	// 	return recipes with ingredient in them
	// }
	
});


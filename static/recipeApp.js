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



const filter_input = document.getElementById('ingredient_filter');
// const recipe_cards = document.querySelectorAll('.card');



filter_input.addEventListener("keyup", (evt) => {
	evt.preventDefault();
	if (evt.keyCode === 13) {
		filter_input.click();



		let recipe_cards = $('.card').get()
			let ingredient = filter_input.value;
			
			for (const recipe of recipe_cards){
				console.log(recipe);
				console.log(recipe.textContent);
				if (recipe.textContent.includes(ingredient)) {		
					recipe.hidden = false;
			    }
			    else {
			   	 	recipe.hidden = true;
			    }
				
				
			}


	}
});
		// $('.card')





		// let filtered_recipes = recipe_cards.filter(each_card => each_card.textContent == ingredient); 
		// console.log(filtered_recipes)

		// (task){
			// return recipe_cards.textContent == ingredient;
		// });

			// if (text.includes(ingredient))
			// if ingredient in text:
					// make div disappear from screen




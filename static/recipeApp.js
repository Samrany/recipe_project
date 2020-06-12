"use strict";


$('.recipe_card').on('click', (evt) => {
	evt.preventDefault();

	let recipe_id = evt.currentTarget.name
	evt.currentTarget.innerHTML = "Liked!"


	console.log(evt)
	console.log(evt.currentTarget.name)
	console.log(evt.currentTarget.innerHTML)
	// let recipe = document.getElementById('.recipe_card')
	// console.log(recipe)
	
	// recipe.innerHTML = "Liked!"
	// let recipe_id = recipe.name
		
	
	$.post('/user_fave', {'recipe_id':recipe_id}, (response) =>{
		// liked button. if
	});
});



	

		// $('#name-field').val(),
// f"hi my name is {name}"
//  hi my name is {name} 
// `
// `  ^ part of URL instead of part of body /user_fave/1. get in URL. Post in body.


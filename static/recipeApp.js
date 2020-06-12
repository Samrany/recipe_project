"use strict";


$('#recipe_card').on('click', (evt) => {
	evt.preventDefault();

	let recipe = document.getElementById('recipe_card');
	// console.log(recipe)
	recipe.innerHTML = "Liked!";
	let recipe_id = recipe.name;
	// console.log(recipe.name);
	

		// $('#name-field').val(),



	$.post('/user_fave', recipe_id, (response) =>{




	});
});


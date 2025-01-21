

const bodyContent = document.querySelector("#bodyContent");
let requestDiv = document.querySelector("#requests");
let formsDiv = document.querySelector("#forms");
let declarsDiv = document.querySelector("#declares");


requestDiv.onclick = (event) => {
	requestContent();

}

function requestContent()
{
	bodyContent.innerText = "";
	fetch('api/content/requests', headers = {
		'Content-Type': 'application/json'
	}).then(response => response.json()).then(data => {
		let titleDiv = document.createElement('div');
		let titleH = document.createElement('h2');
		titleDiv.classList.add('row')
		titleH.innerText = "طلبات خطية";
		
		bodyContent.classList.add('column');
		let requestForm = document.createElement('form');
		requestForm.classList.add('box');
		createFormElement('عنوان الطلب', '#title', requestForm);
		createFormElement('الإسم و اللقب', '#name', requestForm);
		createFormElement('العنوان', '#address', requestForm);
		createFormElement('رقم الهاتف', '#number', requestForm);
		titleDiv.appendChild(titleH);
		bodyContent.appendChild(titleDiv);
		bodyContent.appendChild(requestForm)
		
	}).catch(error => console.log(error))
	return;
}

function createFormElement(label, name, parentDiv)
{
	let title = document.createElement('label');
	let input = document.createElement('input');
	title.innerText = label;
	input.setAttribute('name', name);
	parentDiv.appendChild(title);
	parentDiv.appendChild(input);
	return;
}
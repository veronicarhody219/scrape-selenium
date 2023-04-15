import data from "./quiz.json" assert {type: "json"};
const quiz = document.querySelector(".quiz");
let dataConvert = Object.entries(data);
console.log(dataConvert);
console.log(data);
let links = Object.values(data.link);
let titles = Object.values(data.title);
let ids = Object.keys(data.link);
console.log(links);
console.log(titles);
console.log(ids);
const arrayOfObjects = ids.map((currentValue, index) => {
  return {
    id: currentValue,
    link: links[index],
    title: titles[index],
  };
});
console.log(arrayOfObjects);
arrayOfObjects.map((item) => {
  let aLink = document.createElement('a')
  let text = document.createTextNode(item.title);
  aLink.setAttribute('href', item.link)
  aLink.appendChild(text)

  let para = document.createElement("p");
  para.appendChild(aLink);
  document.body.appendChild(para);
});

function Fruits() {
  const [fruits, setFruits] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/fruits')
      .then(response => response.json())
      .then(result => {
        setFruits(result);
      });
  }, []);

  // let response = await fetch('/api/fruits');
  // let result = await response.json();
  // setFruits(result);


  if (fruits.length === 0) {
    return <p>Loading...</p>;
  }

  // We can also use map to replace lines 21-25 for a little shorter code:
  // const fruitListItems = fruits.map((fruit) => {
  //   return (<li key={fruit.fruit_id}>{fruit.name}</li>);
  // });

  const fruitListItems = [];

  for (const fruit of fruits) {
    fruitListItems.push(<li key={fruit.fruit_id}>{fruit.name}</li>);
  }

  return <ul>{fruitListItems}</ul>;
}

ReactDOM.render(<Fruits />, document.querySelector('#root'));

function FetchWeatherButton() {
  function alertWeather() {
    fetch('/api/weather')
      .then(response => response.json())
      .then(data => {
        alert(`The weather will be ${data.forecast}`);
      });
  }

  return (
    <button type="button" onClick={alertWeather}>
      Get Weather with Fetch
    </button>
  );
}

ReactDOM.render(
  <div>
    <FetchWeatherButton />
  </div>,
  document.querySelector('#root')
);

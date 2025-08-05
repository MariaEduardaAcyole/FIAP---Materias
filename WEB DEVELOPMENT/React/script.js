console.log('Hello World')

// const root = document.getElementById('root')
// root.textContent = 'Hello'

const App = () => {
    return React.createElement('h1', null, 'Hellow')
}

ReactDOM.render(
    React.createElement(App),
    document.getElementById('root')
)


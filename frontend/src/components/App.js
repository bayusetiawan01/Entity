import React, { Component } from "react";
import { render, Render } from "react-dom";
export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return <h1>Testing</h1>
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
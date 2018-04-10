import React from "react";
import Charts from "./Charts";
import { PageHeader } from "react-bootstrap";


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.ids = ["1", "2", "3", "4", "5"];

        this.render = this.render.bind(this);
    }

    render () {
        return (
            <div className="container>">
                <Charts ids={this.ids}/>
            </div>
        );
    }
}

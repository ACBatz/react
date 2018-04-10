import React from "react";
import Chart from "./Chart";
import Columns from "react-columns"

export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.ids = props.ids;

        this.render = this.render.bind(this);
    }

    render () {
        return (
            <Columns columns="3">
                {this.ids.map(id => {return (<Chart id={id} />)})}
            </Columns>
        );
    }
}

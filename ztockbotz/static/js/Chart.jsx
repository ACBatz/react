import React from "react";
import vis from "vis";

require('../css/vis-timeline-graph2d.min.css');

export default class Chart extends React.Component {
    constructor(props) {
        super(props);
        this.id = this.props.id;
        this.DELAY = 100;
        this.strategy = "static";
        this.dataset = new vis.DataSet();
        this.options = {
            start: vis.moment().add(-30, 'seconds'), // changed so its faster
            end: vis.moment(),
            dataAxis: {
                left: {
                    range: {
                        min:-10, max: 10
                    }
                }
            },
            drawPoints: {
                style: 'circle' // square, circle
            },
            shaded: {
                orientation: 'bottom' // top, bottom
            }
        };

        this.componentDidMount = this.componentDidMount.bind(this);
        this.renderStep = this.renderStep.bind(this);
        this.addDataPoint = this.addDataPoint.bind(this);
    }

    componentDidMount() {
        this.container = document.getElementById(this.id);
        this.graph2d = new vis.Graph2d(this.container, this.dataset, this.options);
        this.renderStep();
        this.addDataPoint();
    }

    y(x) {
        return (Math.sin(x / 2) + Math.cos(x / 4)) * 5;
    }
    renderStep() {
        // move the window (you can think of different strategies).
        var now = vis.moment();
        var range = this.graph2d.getWindow();
        var interval = range.end - range.start;
        if (now > range.end) {
            this.graph2d.setWindow(now - 0.1 * interval, now + 0.9 * interval);
        }
        setTimeout(this.renderStep, this.DELAY);
    }

    addDataPoint() {
        // add a new data point to the dataset
        var now = vis.moment();
        this.dataset.add({
            x: now,
            y: this.y(now / 1000)
        });

        // remove all data points which are no longer visible
        var range = this.graph2d.getWindow();
        var interval = range.end - range.start;
        var oldIds = this.dataset.getIds({
            filter: function (item) {
                return item.x < range.start - interval;
            }
        });
        this.dataset.remove(oldIds);

        setTimeout(this.addDataPoint, this.DELAY);
    }

    render () {
        return (
            <div id={this.id}></div>
        );
    }
}

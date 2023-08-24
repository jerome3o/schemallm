console.log('Hello World');


// Define the dimensions of your visualization
const WIDTH = 600;
const HEIGHT = 400;
const NTOKENS = 20;

let data = {};

$.getJSON("/data/infographic_data.json", function(response) {
    data = response;
    $("#stepSlider").attr("max", data.steps.length - 1);
    updateVisualization(0);
});


$("#stepSlider").on("input", function(e) {
    updateVisualization(parseInt(e.target.value));
});

function updateVisualization(step) {
    console.log(step);
}

function updateVisualization(stepIndex) {
    const stepData = data.steps[stepIndex];

    // Update the text preview
    $("#partialCompletionText").text(stepData.partial_completion);
    $("#selectedTokenText").text(stepData.selected_token);

    // Update the bar plot, todo
    updateBarPlot(stepData);
}

function updateBarPlot(stepData) {
    // take first 10 tokens and probabilities
    let trace = {
        x: stepData.tokens.slice(0, NTOKENS),
        y: stepData.probabilities.slice(0, NTOKENS),
        type: 'bar'
    }
    let yRange = [0, 1];

    let layout = {
        title: 'Token Probabilities',
        xaxis: { title: 'Tokens' },
        yaxis: { title: 'Probabilities' , range: yRange},
    };

    Plotly.react('barContainer', [trace], layout);
}


// Load data
d3.json("cleaned_scored_tweets.json").then(function(data){
    // Initialize dictionary for word count
    var wordCounts = {}
    for (i = 0; i < data.length; i++) {
        // Get value of "string_text" key
        var arrayOfWords = data.map(value => value.text)
    }
    arrayOfWords.forEach(function(list) {
        // Iterate through each word to add to dictionary
        list.forEach(function(word) {
            // Add word if not in dictionary and put 1 as value
            if (!wordCounts[word]) {
                wordCounts[word] = 1;
            } else {
                // Add count if word is already in dictionary
                wordCounts[word]++;
            }
        })
    })

    // Create items array
    var items = Object.keys(wordCounts).map(function(key) {
        return [key, wordCounts[key]];
    });
    
    // Sort the array based on the second element
    items.sort(function(first, second) {
        return second[1] - first[1];
    });

    // Create a new array with only the first 100 / 10 items
    var topWordsCloud = items.slice(1, 101)
    var topWords = items.slice(1, 11)
    console.log(topWords)

    // Create the yticks for the bar chart.
    var yticks = topWords.map(function(word){
        return word[0]}).reverse()
    var wordValues = topWords.map(function(word){
        return word[1]}).reverse()
    //var wordLabels = topWords[0]

    // Create the trace for the bar chart. 
    var barData = [{
      type: "bar",
      x: wordValues,
      y: yticks,
      //text: wordLabels,
      orientation: "h"
    }];

    // Create the layout for the bar chart. 
    var barLayout = {
      title: "Top 10 Words",
      titlefont: {"size": 22},
      width: 800,
      height: 800,
      xaxis: {range: [0, 15000]},
      yaxis: {range: [0, 10]}
    };
    // Use Plotly to plot the data with the layout. 
    Plotly.newPlot("bar", barData, barLayout);

    // Tag Cloud
    anychart.onDocumentReady(function() {
        // set size
        var stage = anychart.graphics.create("cloud", 800, 600);
        // create a tag (word) cloud chart
        var chart = anychart.tagCloud(topWordsCloud);
        // set a chart title
        chart.title('Top 100 Words')
        // set an array of angles at which the words will be laid out
        chart.angles([0])
        // set the mode of the tag cloud
        chart.mode("spiral");     
        // display the word cloud chart
        chart.tooltip(false);
        chart.container(stage).draw();
    });

});

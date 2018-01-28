/*var svg = d3.select("svg"),
    margin = {top: 20, right: 0, bottom: 30, left: 100},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("/../../static/data/data.tsv", function(d) {
  d.frequency = +d.frequency;
  return d;
}, function(error, data) {
  if (error) throw error;

  x.domain(data.map(function(d) { return d.month; }));
  y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y).ticks(10, "%"))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Frequency");

  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.month); })
      .attr("y", function(d) { return y(d.frequency); })
      .attr("width", x.bandwidth())
      .attr("height", function(d) { return height - y(d.frequency); });
});*/

/*d3.json("http://luibasantes.pythonanywhere.com/api/users_stats/", function(error, data) {
  (function() {*/

d3.json('https://d3fc.io/examples/bubble/data.json', function(_, data) {
  // convert string properties to numbers
  data.forEach(function(d) {
    d.income = Number(d.income);
    d.population = Number(d.population);
    d.lifeExpectancy = Number(d.lifeExpectancy);
  });

  var regions = d3.set(data.map(function(d) { return d.region; }));
  var color = d3.scaleOrdinal(d3.schemeCategory10)
    .domain(regions.values());

  var legend = d3.legendColor()
    .scale(color);

  var size = d3.scaleLinear().range([20, 800])
    .domain(fc.extentLinear()
    .accessors([function(d) { return d.population; }])(data));

  var pointSeries = fc.seriesSvgPoint()
      .crossValue(function(d) { return d.income; })
      .mainValue(function(d) { return d.lifeExpectancy; })
      .size(function(d) { return size(d.population); })
      .decorate(function(sel) {
        sel.enter()
            .attr('fill', function(d) { return color(d.region); });
      });

  var chart = fc.chartSvgCartesian(
                d3.scaleLog(),
                d3.scaleLinear()
              )
      .xDomain(fc.extentLinear()
        .accessors([function(d) { return d.income; }])(data))
      .yDomain(fc.extentLinear()
        .accessors([function(d) { return d.lifeExpectancy; }])(data))
      .chartLabel('The Wealth & Health of Nations')
      .xLabel('Income (dollars)')
      .yLabel('Life expectancy (years)')
      .xTicks(2, d3.format(',d'))
      .yOrient('left')
      .plotArea(pointSeries)
      .decorate(function(selection) {
        // append an svg for the d3-legend
        selection.enter()
          .append('svg')
          .attr('class', 'legend');

        // render the legend
        selection.select('.legend')
          .call(legend);
      });

  d3.select('#bubble-chart')
      // remove the loading text from the container
      .text(null)
      .datum(data)
      .call(chart);
});
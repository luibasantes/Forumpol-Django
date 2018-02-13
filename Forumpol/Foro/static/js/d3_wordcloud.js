var fill = d3.scaleOrdinal(d3.schemeCategory20);
var layout = d3.layout.cloud()
.size([500, 500])
.words([{"tag":"math","size:":40},{"tag":"physics","size:":10},{"tag":"algebra","size:":20},{"tag":"chemistry","size:":5},].map(function(d) {
  return {text: d.tag, size: 10 + d.size * 90, test: "haha"};
}))
.padding(5)
.rotate(function() { return ~~(Math.random() * 2) * 90; })
.font("Impact")
.fontSize(function(d) { return d.size; })
.on("end", draw);

layout.start();

function draw(words) {
	d3.select("#wc_div").append("svg")
	  .attr("width", layout.size()[0])
	  .attr("height", layout.size()[1])
	.append("g")
	  .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
	.selectAll("text")
	  .data(words)
	.enter().append("text")
	  .style("font-size", function(d) { return d.size + "px"; })
	  .style("font-family", "Impact")
	  .style("fill", function(d, i) { return fill(i); })
	  .attr("text-anchor", "middle")
	  .attr("transform", function(d) {
	    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
	  })
	  .text(function(d) { return d.text; });
}
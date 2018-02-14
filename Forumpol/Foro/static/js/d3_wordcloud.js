var fill = d3.scaleOrdinal(d3.schemeCategory20);
var layout;

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

$.ajax({
	url: window.location.origin + "/api/recursos/tags_count/",
	type: "GET",
	success: function(json){
	alert(json)
	layout = d3.layout.cloud()
		.size([500, 500])
		.words(json.map(function(d) {
		  return {text: d.tag, size: 10 + d.counts * 10, test: "haha"};
		}))
		.padding(5)
		.rotate(function() { return ~~(Math.random() * 2) * 90; })
		.font("Impact")
		.fontSize(function(d) { return d.size; })
		.on("end", draw);

	layout.start();
	}
});


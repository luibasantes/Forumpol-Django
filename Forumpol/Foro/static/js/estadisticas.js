function comparar ( a, b ){ return a.valor - b.valor; }





var data = [];
var maximo=0;


var metodoGet = $.getJSON( 'http://luibasantes.pythonanywhere.com/api/users_stats/', function( json ) {
    $.each( json, function( key, val ) {
        data.push({usuario:val.nombre_usuario,valor:Number(val.numero_posts)});
        if(Number(val.numero_posts)>maximo){
            maximo=Number(val.numero_posts);
        }
    });
    data.sort( comparar );
    console.log(data);
});




metodoGet.done(function(){

    var altura = data.length *50 + 30
    var anchura = 960
    var widthscale = d3.scale.linear()
      .domain([0,maximo])
      .range([0, anchura-20]);

    var color = d3.scale.linear()
      .domain([0, maximo])
      .range(['red','blue']);

    var axis = d3.svg.axis().ticks(10).scale(widthscale);

    var canvas = d3.select('#Grafico')
                .append('svg')
                .attr('width',anchura)
                .attr('height',altura)
                .append('g');


    var bars = canvas.selectAll("rect")
            .data(data)
            .enter()
                .append("rect")
                .attr('width',function(d) { return widthscale(d.valor) + 'px' })
                .attr('height',25)
                .attr('y',function(d,i) { return i*50  })
                .attr('fill',function(d) { return 'lightblue'});

    var usuarios = canvas.selectAll("text")
            .data(data)
            .enter()
                .append("text")
                .attr('y',function(d,i) { return i*50 + 20})
                .attr('fill',function(d) { return 'black'})
                .text(function(d) { return d.usuario; });



    canvas.append('g').attr('transform','translate(3,'+data.length *50+')').call(axis);
});


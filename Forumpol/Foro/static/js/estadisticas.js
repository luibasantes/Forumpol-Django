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
    var widthscale = d3.scaleLinear()
      .domain([0,maximo])
      .range([0, anchura-20]);

    var color = d3.scaleLinear()
      .domain([0, maximo])
      .range(['red','blue']);


    var axis = d3.axisBottom(widthscale).ticks(10)
    //var axis = d3.svg.axis().ticks(10).scale(widthscale);

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



    var altura = 500
    var anchura = 960

    var radiusScale = d3.scaleSqrt().domain([1,20]).range([30,150])

    var canvasB = d3.select('#GraficoCloud')
                    .append('svg')
                    .attr('width',anchura)
                    .attr('height',altura)
                    .append('g')
                    .attr('transform','translate(0,0)');


    var forceCollide = d3.forceCollide(function(d){
                        return radiusScale(Number(d.numero_posts)+1)
                    });

    var simulation = d3.forceSimulation()
                    .force("x",d3.forceX(anchura / 2).strength(0.05))
                    .force('y',d3.forceY(altura / 2).strength(0.05))
                    .force('collide',forceCollide)

    var texto = canvasB.selectAll('text')
                    .data(data)
                    .enter()
                        .append("text")
                        .text( function (d) { return d.nombre_usuario })
                        .attr("font-family", "sans-serif")
                        //.attr('font-size',function(d) { return radiusScale(Number(d.numero_posts)+1)+"px"})
                        .attr('font-size',function (d) { return Number(d.numero_posts)+1})
                        .attr("fill", "red");


    simulation.nodes(data)
        .on("tick", tick);

    function tick(){
        texto
            .attr("x",function(d) { return d.x})
            .attr("y",function(d) { return d.x})
            .on('click',function(d){
                alert("El usuario: "+d.nombre_usuario + " tiene " + d.numero_posts + " aportaciones.")
            })
    }

});

var altura = 700
var anchura = 960







d3.json('http://luibasantes.pythonanywhere.com/api/users_stats/',function(dataUsers){



   var canvas = d3.select('#GraficoBubble')
                    .append('svg')
                    .attr('width',anchura)
                    .attr('height',altura)
                    .append('g')
                    .attr('transform','translate(0,0)')

    var defs = canvas.append("defs");

    defs.append("pattern")
        .attr("id","profilePic")
        .attr("height","100%")
        .attr("width","100%")
        .attr("patternContentUnits","objectBoundingBox")
        .append("image")
        .attr("height",1)
        .attr("width",1)
        .attr("preserveAspectRatio","none")
        .attr("xmlns:xlink","https://www.w3.org/1999/xlink")
        .attr("xlink:href","http://luibasantes.pythonanywhere.com/media/profile_image/10/tumblr_of5yep42e11ugp61po1_500.gif")



    var radiusScale = d3.scaleSqrt().domain([1,20]).range([30,150])

    var forceXSplit = d3.forceX(function(d){
                        if(d.moderador){
                            return anchura -300
                        }else{
                            return 200
                        }
                    }).strength(0.09);

    var forceXCombine = d3.forceX(anchura / 2).strength(0.09);

    var forceY = d3.forceY(function(d){
                        return altura / 2
                    }).strength(0.05);

    var forceCollide = d3.forceCollide(function(d){
                        return radiusScale(Number(d.numero_posts)+1)
                    });

    var simulation = d3.forceSimulation()
                    .force("x",d3.forceX(anchura / 2).strength(0.08))
                    .force('y',forceY)
                    .force('collide',forceCollide)

    var circles = canvas.selectAll('.artist')
                    .data(dataUsers)
                    .enter()
                        .append('circle')
                        .attr('class','artist')
                        .attr('r',function(d) { return radiusScale(Number(d.numero_posts)+1)})
                        //.attr('r',10)
                        .attr('fill',function(d) { return "url(#"+d.nombre_usuario+")"})

    defs.selectAll(".artist-pattern")
        .data(dataUsers)
        .enter().append("pattern")
            .attr('class','artist-pattern')
            .attr("id",function(d) { return d.nombre_usuario})
            .attr("height","100%")
            .attr("width","100%")
            .attr("patternContentUnits","objectBoundingBox")
            .append("image")
            .attr("height",1)
            .attr("width",1)
            .attr("preserveAspectRatio","none")
            .attr("xmlns:xlink","https://www.w3.org/1999/xlink")
            .attr("xlink:href",function(d) {
                if(d.image==null){
                    return "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png"
                }else{
                    return "http://luibasantes.pythonanywhere.com"+d.image
                }
            })


    d3.select("#decade").on("click",function(){
        simulation.force("x",forceXSplit)
            .alphaTarget(0.5)
            .restart();
    })

    d3.select("#combine").on("click",function(){
        simulation.force("x",forceXCombine)
            .alphaTarget(0.5)
            .restart();
    })

    simulation.nodes(dataUsers)
        .on("tick", tick);

    function tick(){
        circles
            .attr("cx",function(d) { return d.x})
            .attr("cy",function(d) { return d.y})
            .on('click',function(d){
                alert("El usuario: "+d.nombre_usuario + " tiene " + d.numero_posts + " aportaciones.")
            })
    }
});




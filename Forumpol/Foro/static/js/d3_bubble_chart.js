var contadorA=0
var contadorE=0
var contadorC=0
var data2 = ["Anuncios","Clubs Espol","Vida Estudiantil"]
var data3= []
var r = 200
var altura1 = 500
var anchura1 = 960
var metodoGet2 = $.getJSON( 'http://luibasantes.pythonanywhere.com/api/threads/all/', function( json ) {

    $.each( json, function( key, val ) {
        if(val.category=='anuncio'){
            contadorA++;
        }else if(val.category=='clubs_espol'){
            contadorC++;
        }else{
            contadorE++;
        }
    });
    data3= [contadorA,contadorC,contadorE]
});

metodoGet2.done(function(){

    var color = d3.scaleOrdinal()
                    .range(['red','blue','orange']);

    var canvas = d3.select('#Grafico')
                .append('svg')
                .attr('width',anchura1)
                .attr('height',altura1);


    var group = canvas.append('g')
                    .attr("transform","translate(480,250)");


    var arc = d3.arc()
                .innerRadius(0)
                .outerRadius(r);
    var pie = d3.pie()
                .value(function(d) {return d;});

    var arcs = group.selectAll(".arcs")
                    .data(pie(data3))
                    .enter()
                    .append("g")
                        .attr("class","arc");

    arcs.append("path")
        .attr("d",arc)
        .attr("fill",function(d){return color(d.data)});
    arcs.append("text")
        .attr("transform",function(d) { return "translate("+arc.centroid(d)+")" ;})
        .attr("text-anchor","middle")
        .attr("font-size","1.5em")
        .text(function(d){return d.data});
    canvas.append("g")
        .attr("transform","translate(700,250)")
        .selectAll(".categorias")
            .data(pie(data2))
            .enter()
                .append("text")
                .attr("transform",function(d){
                    if(d.data == "Anuncios"){
                        return "translate(0,0)";
                    }else if(d.data == "Clubs Espol"){
                        return "translate(0,20)";
                    }else{
                        return "translate(0,40)";
                    }
                })
                .text(function(d){
                    if(d.data == "Anuncios"){
                        return d.data + "    color: Rojo" ;
                    }else if(d.data == "Clubs Espol"){
                        return d.data + "   color: Azul";
                    }else{
                        return d.data + "  color: Naranja";
                    }
                });
});
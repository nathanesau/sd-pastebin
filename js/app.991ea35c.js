(function(t){function e(e){for(var r,i,s=e[0],c=e[1],u=e[2],p=0,f=[];p<s.length;p++)i=s[p],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&f.push(a[i][0]),a[i]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);l&&l(e);while(f.length)f.shift()();return o.push.apply(o,u||[]),n()}function n(){for(var t,e=0;e<o.length;e++){for(var n=o[e],r=!0,s=1;s<n.length;s++){var c=n[s];0!==a[c]&&(r=!1)}r&&(o.splice(e--,1),t=i(i.s=n[0]))}return t}var r={},a={app:0},o=[];function i(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.m=t,i.c=r,i.d=function(t,e,n){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)i.d(n,r,function(e){return t[e]}.bind(null,r));return n},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/sd-pastebin/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=e,s=s.slice();for(var u=0;u<s.length;u++)e(s[u]);var l=c;o.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";var r=n("85ec"),a=n.n(r);a.a},"403d":function(t,e,n){},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("PasteArea")],1)},o=[],i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"pastearea"},["new"===t.type?n("div",[n("h1",[t._v(" New paste ")]),n("br"),n("form",{on:{submit:function(e){return e.preventDefault(),t.write_paste(e)}}},[n("textarea",{directives:[{name:"model",rawName:"v-model",value:t.content,expression:"content"}],attrs:{rows:"20,",cols:"100,",name:"pastearea"},domProps:{value:t.content},on:{input:function(e){e.target.composing||(t.content=e.target.value)}}}),n("br"),n("br"),n("button",{staticClass:"button"},[t._v("Submit")])]),n("br"),t.shortlink?n("p",[t._v(" Your content can be found at: "),n("a",{attrs:{href:t.url_link}},[t._v(t._s(t.url_link))])]):t._e()]):t._e(),"existing"===t.type?n("div",[n("h1",[t._v(t._s(t.shortlink))]),n("textarea",{staticStyle:{"background-color":"light-grey"},attrs:{rows:"20,",cols:"100",readonly:""},domProps:{value:t.content}}),n("ul",[n("li",[t._v("Created at: "+t._s(t.created_at))]),n("br"),n("br"),n("li",[t._v("Expires at: "+t._s(t.expires_at))]),n("br"),n("br")])]):t._e()])},s=[],c=(n("d3b7"),n("ac1f"),n("3ca3"),n("841c"),n("ddb0"),n("2b3d"),n("96cf"),n("1da1")),u=n("bc3a"),l=n.n(u),p={name:"Paste",data:function(){return{type:"new",content:"",shortlink:"",url_link:""}},created:function(){var t=window.location.search.substring(1),e=new URLSearchParams(t);e.get("shortlink")&&(this.type="existing",this.shortlink=e.get("shortlink"),this.urllink=t,this.created_at="",this.expires_at="",this.get_data(this.shortlink))},methods:{write_paste:function(){var t=this;return Object(c["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:n={expiration_length_in_minutes:"43200",paste_contents:t.content},l.a.post("https://api.pastebin.io/pastebin-api/api/v1/paste",JSON.stringify(n),{headers:{"Content-Type":"application/json"}}).then((function(e){t.shortlink=e.data.shortlink;var n=window.location;t.url_link=n.origin+"/sd-pastebin?shortlink="+t.shortlink})).catch((function(t){return console.log(t)}));case 2:case"end":return e.stop()}}),e)})))()},get_data:function(t){var e=this;return Object(c["a"])(regeneratorRuntime.mark((function n(){var r;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:r=l.a.get("https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink="+t,{headers:{"Content-Type":"application/json"}}),Promise.all([r]).then((function(t){e.content=t[0].data.paste_contents,e.created_at=t[0].data.created_at,e.expires_at=t[0].data.expires_at}));case 2:case"end":return n.stop()}}),n)})))()}}},f=p,d=(n("f2ac"),n("2877")),h=Object(d["a"])(f,i,s,!1,null,"37b649d0",null),b=h.exports,v={name:"App",components:{PasteArea:b}},_=v,g=(n("034f"),Object(d["a"])(_,a,o,!1,null,null,null)),m=g.exports;r["a"].config.productionTip=!1,new r["a"]({render:function(t){return t(m)}}).$mount("#app")},"85ec":function(t,e,n){},f2ac:function(t,e,n){"use strict";var r=n("403d"),a=n.n(r);a.a}});
//# sourceMappingURL=app.991ea35c.js.map
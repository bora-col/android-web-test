(this["webpackJsonpsmart-door-lock-frontend"]=this["webpackJsonpsmart-door-lock-frontend"]||[]).push([[4],{199:function(e,t,a){e.exports=a.p+"static/media/logo-white.ea793549.svg"},204:function(e,t,a){e.exports=a.p+"static/media/door_open.680857cc.svg"},205:function(e,t,a){e.exports=a.p+"static/media/door_close.1d5ab1f4.svg"},206:function(e,t,a){e.exports=a.p+"static/media/door_disconnect.f195aeac.svg"},207:function(e,t,a){e.exports=a.p+"static/media/door_close_locked.c2435e8c.svg"},228:function(e,t,a){e.exports=a.p+"static/media/biss_logo.eb4b2ff4.svg"},229:function(e,t,a){e.exports=a.p+"static/media/dashboard.689b12e4.svg"},280:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),o=a(159),i=a(34),c=a(169),E=a(2);function _(e){var t=Object(i.b)(),a=Object(i.c)((function(e){return e.snackbar})),n=Object(i.c)((function(e){return e.language.menu})),r=Object(c.useSnackbar)().enqueueSnackbar;return a.show&&(r(n.get(a.message),{variant:a.messageType}),t((function(e){return e({type:E.j})}))),null}var s=a(271),l=a(163),R=Object(l.a)((function(e){return{appBar:{zIndex:e.zIndex.drawer+1,backgroundColor:e.palette.primary.main,width:"100%"},hide:{display:"none"},title:{flexGrow:1,textAlign:"center"},icon:{color:"white"},logoMenu:{width:150,height:60,paddingTop:0,paddingBottom:0}}})),d=a(199),S=a.n(d),u=a(273),m=a(274),p=a(275);function O(e){var t=R();return r.a.createElement(u.a,{position:"fixed",className:t.appBar},r.a.createElement(m.a,null,r.a.createElement(p.a,{variant:"h5",noWrap:!0,className:t.title},r.a.createElement(o.b,{to:"/"},r.a.createElement("img",{src:S.a,alt:"logo",className:t.logoMenu})))))}var g={Application:{header:"Biss Smart Lock",copyright:"\xa9 Copyright 2020 Bosphorus Industrial Software Solutions"}},T=Object(l.a)((function(e){return{title:{flexGrow:1,textAlign:"center",color:"rgb(255, 255, 255)"},toolbar:{minHeight:40},appBar:{top:"auto",bottom:0,zIndex:e.zIndex.drawer+2,height:40,backgroundColor:e.palette.primary.main}}}));function f(){var e=T();return r.a.createElement("div",null,r.a.createElement(u.a,{className:e.appBar},r.a.createElement(m.a,{className:e.toolbar},r.a.createElement(p.a,{m:1,className:e.title},g.Application.copyright))))}var P=a(37),N=a(31),h=a(141),A=Object(l.a)((function(e){return{overview:{fontSize:50,color:e.palette.text.secondary}}})),b=a(251),v=a(281),I=a(204),D=a.n(I),w=a(205),x=a.n(w),C=a(206),U=a.n(C),y=Object(l.a)((function(e){return{imgSize:{width:"100%",marginTop:30},logImgSize:{width:"100%"},box:{padding:16,backgroundColor:e.palette.primary.lightGray,color:e.palette.text.primary,height:"33vh",boxShadow:e.palette.primary.boxShadow},tableContainer:{height:"100%"},boxHeader:{fontSize:45,fontWeight:300},fontChildProperty:{fontSize:30,fontWeight:300},doorStatusItem:{fontSize:35,fontWeight:300,marginTop:10,marginBottom:16},userNumberFont:{fontSize:50,fontWeight:300,marginTop:-5},logTable:{marginTop:50,marginLeft:-30}}})),M=a(207),G=a.n(M),j={MODE:"dev",DEV_URL:"http://35.194.42.231:4444",PROD_URL:"".concat(window.location.origin,"/api"),REQUEST_TIMEOUT:3e3,REQUEST_TIMEOUT_ERROR_MESSAGE:"timeout of 3000ms exceeded",DOOR_STATUS:{OPEN_UNLOCK:0,CLOSE_UNLOCK:1,CLOSE_LOCK:2,BUSY:3,WAITING:4,UNKNOWN:-1}};var k=a(208),L=a.n(k).a.create({baseURL:"prod"===j.MODE?j.PROD_URL:j.DEV_URL,timeout:j.REQUEST_TIMEOUT});"dev"===j.MODE&&L.interceptors.response.use((function(e){return e}));var Y=L,K=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:2,t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:1;return{url:"/door_status?office_id=".concat(t,"&id=").concat(e),method:"get"}},B={RSP_TYPE_REQUEST_FAILED:900,RSP_TYPE_INTERNAL_SERVER_ERROR:500,RSP_TYPE_ERR_INVALID_TOKEN:600,RSP_TYPE_ERR_NETWORK_ERR:700,RSP_TYPE_ERR_TIMEOUT_ERR:701,RSP_MESSAGE_ERR_REQUEST_TIME_OUT:"Request Time Out Error !",RSP_MESSAGE_ERR_NETWORK_ERR:"Server is not available",RSP_MESSAGE_REQUEST_FAILED:"Network error, please try again.",RSP_MESSAGE_INTERNAL_SERVER_ERROR:"Server Error!",RSP_MESSAGE_INVALID_TOKEN:"Authentication failed.",RSP_MESSAGE_ERR_TIMEOUT_ERR:"Timeout Error !",RSP_TYPE_SUCCESS:100,RSP_TYPE_ERR_TOKEN_EXPIRED:101,RSP_TYPE_ERR_TOKEN_IS_NOT_VALID:102,RSP_TYPE_ERR_TOKEN_IS_NOT_GENERATED:103,RSP_TYPE_ERR_TOKEN_IS_VERIFIED:104,RSP_TYPE_ERR_TOKEN_IS_NOT_MATCH_WITH_USER:105,RSP_TYPE_ERR_USER_NOT_FOUND:106,RSP_TYPE_ERR_USER_PASSWORD_NOT_CORRECT:107,RSP_TYPE_ERR_DATABASE_ERROR:108,RSP_TYPE_ERR_DATABASE_CONNECTION_ERROR:109,RSP_TYPE_ERR_DATABASE_QUERY_ERROR:110,RSP_TYPE_ERR_DOOR_NOT_FOUND:110,RSP_TYPE_ERR_DOOR_INFO_COULD_NOT_UPDATED:111,RSP_TYPE_ERR_DOOR_NOT_CONNECTED:112,RSP_TYPE_ERR_UNAUTHORIZED:113,RSP_TYPE_ERR_INVALID_MODEL:114,RSP_TYPE_ERR_INVALID_CLIENT:114,RSP_TYPE_ERR_PASSWORD_CHANGE_REQUIRED:115,RSP_TYPE_INCORRECT_ALERT_PASSWORD:116,RSP_TYPE_DOOR_BUSY:117,RSP_TYPE_ERR_UNKNOWN:800,RSP_TYPE_DEV_MODE:801,RSP_MESSAGE_COMPLETED:"Request Completed",RSP_MESSAGE_USER_NOT_FOUND:"User not found!",RSP_MESSAGE_WRONG_PASSWORD_OR_MAIL:"Username or password is not correct!",RSP_MESSAGE_TOKEN_COULDNOT_GENERATED:"Error occured when generating token!",RSP_MESSAGE_TOKEN_EXPIRED:"Given token is expired!",RSP_MESSAGE_TOKEN_IS_NOT_VALID:"Given token is not valid!",RSP_MESSAGE_TOKEN_IS_NOT_MATCH_WITH_USER:"Given token is not matched with given user!",RSP_MESSAGE_DOOR_OPEN_COMMAND_SENT:"Door open command was sent the doors.",RSP_MESSAGE_DOOR_LOCK_COMMAND_SENT:"Door lock command was sent the doors.",RSP_MESSAGE_DOOR_FOUND:"Door is found!",RSP_MESSAGE_DOOR_NOT_FOUND:"Door is not found!",RSP_MESSAGE_DOOR_INFO_COULD_NOT_UPDATED:"Door informations could not be updated!",RSP_MESSAGE_ERR_DOOR_NOT_CONNECTED:"Door is not connected to server!",RSP_MESSAGE_ERR_UNAUTHORIZED:"User does not have permission.",RSP_MESSAGE_ERR_INVALID_MODEL:"Given model is invalid.",RSP_MESSAGE_ERR_INVALID_CLIENT:"Client version is not valid.",RSP_MESSAGE_ERR_PASSWORD_CHANGE_REQUIRED:"User's password needs to be changed.",RSP_MESSAGE_INCORRECT_ALERT_PASSWORD:"Alert password is incorrect.",RSP_MESSAGE_DOOR_BUSY:"Door is busy with processing command."},W=a(55);var z=!1;function V(e,t){return q(K(e,t))}function H(){W.a.dispatch((function(e){e({type:E.g})}))}function F(e){W.a.dispatch(function(e){return function(t){t({type:E.a,data:e})}}(e))}function Q(){W.a.dispatch((function(e){e({type:E.d})}))}function q(e){return Y(e).then((function(t){var a=t&&t.data&&t.data.status;if(t&&t.data)if(a===B.RSP_TYPE_ERR_UNKNOWN||a===B.RSP_TYPE_ERR_DATABASE_ERROR||a===B.RSP_TYPE_ERR_DATABASE_CONNECTION_ERROR||a===B.RSP_TYPE_ERR_DATABASE_QUERY_ERROR||a===B.RSP_TYPE_ERR_TOKEN_IS_NOT_GENERATED)z=!0,console.log("Internal Server Error:",t.data.data),F({message:B.RSP_MESSAGE_INTERNAL_SERVER_ERROR,status:B.RSP_TYPE_INTERNAL_SERVER_ERROR});else{if(a!==B.RSP_TYPE_ERR_TOKEN_EXPIRED&&a!==B.RSP_TYPE_ERR_TOKEN_IS_NOT_VALID&&a!==B.RSP_TYPE_ERR_TOKEN_IS_NOT_MATCH_WITH_USER)return z&&(z=!1,H()),t;console.log("Token is expired, login required."),"/user/info"!==e.url&&Q()}else console.log("Error: Http request failed!"),z=!0,F({message:B.RSP_MESSAGE_REQUEST_FAILED,status:B.RSP_TYPE_REQUEST_FAILED})})).catch((function(e){"Network Error"===e.message?(console.log("network error"),z=!0,F({message:B.RSP_RSP_MESSAGE_ERR_NETWORK_ERR,status:B.RSP_TYPE_ERR_NETWORK_ERR})):e.message===j.REQUEST_TIMEOUT_ERROR_MESSAGE?(z=!0,F({message:B.RSP_MESSAGE_ERR_TIMEOUT_ERR,status:B.RSP_TYPE_ERR_TIMEOUT_ERR})):(console.log("Unhandled http error:",e),Promise.reject(e))}))}var X=j.DOOR_STATUS,J=function(e){switch(e){case X.CLOSE_UNLOCK:return x.a;case X.OPEN_UNLOCK:return D.a;case X.CLOSE_LOCK:return G.a;default:return U.a}},Z=function(e,t){var a=new Date(Date.now());e(a.toLocaleDateString()),t(a.toLocaleTimeString())};function $(){var e=y(),t=Object(i.b)(),a=Object(i.c)((function(e){return e.language.menu})),o=Object(i.c)((function(e){return e.error.status})),c=a.get("OverviewPage.doorCardTitle"),_=Object(n.useState)(null),s=Object(b.a)(_,2),l=s[0],R=s[1],d=Object(n.useState)(null),S=Object(b.a)(d,2),u=S[0],m=S[1],O=Object(n.useState)(-1),g=Object(b.a)(O,2),T=g[0],f=g[1],P=a.get("OverviewPage.door".concat(T)),N=Object(n.useRef)(null);return Object(n.useEffect)((function(){o?clearInterval(N.current):N.current=setInterval((function(){V().then((function(e){e&&(f(e.data.data),Z(R,m))}))}),1e3)}),[o]),Object(n.useEffect)((function(){return t((function(e){e({type:E.r})})),V().then((function(e){e&&(f(e.data.data),Z(R,m),t((function(e){e({type:E.i})})))})),function(){clearInterval(N.current)}}),[t]),r.a.createElement(v.a,{className:e.box},r.a.createElement(h.a,{container:!0,direction:"row"},r.a.createElement(h.a,{item:!0,container:!0,xs:9,direction:"column"},r.a.createElement(h.a,{item:!0,className:e.boxHeader},c),r.a.createElement(h.a,{item:!0,className:e.doorStatusItem},P),r.a.createElement(h.a,{item:!0,container:!0,direction:"column"},r.a.createElement(h.a,{item:!0,className:e.fontChildProperty},l),r.a.createElement(h.a,{item:!0,className:e.fontChildProperty},u))),r.a.createElement(h.a,{item:!0,xs:3,container:!0,justify:"flex-end"},r.a.createElement(p.a,{variant:"h5",noWrap:!0},r.a.createElement("img",{className:e.imgSize,src:J(T),alt:"door-"+T})))))}function ee(){var e=A(),t=Object(i.c)((function(e){return e.language.menu}));return r.a.createElement(h.a,{container:!0,direction:"column"},r.a.createElement(h.a,{item:!0,xs:12,className:e.overview},t.get("OverviewPage.pageTitle")),r.a.createElement(h.a,{item:!0,container:!0,direction:"row",spacing:3},r.a.createElement(h.a,{item:!0,xs:12,md:6,justify:"center"},r.a.createElement($,null))))}var te=a(228),ae=a.n(te),ne=(a(67),a(41)),re=a(284),oe=a(276),ie=Object(l.a)((function(e){return{text:{marginTop:-50},backdrop:{zIndex:e.zIndex.drawer+1,color:"#ffffff"}}}));function ce(e){var t=ie();return r.a.createElement("div",{style:{display:"flex",justifyContent:"center",alignItems:"center",height:"98vh",position:"relative"}},r.a.createElement(ne.Animated,{animationIn:"fadeIn",animationOut:"fadeOut",animationInDuration:1500,animationOutDuration:1e3,isVisible:!0},r.a.createElement("img",{src:ae.a,alt:"loadingScreen",style:{height:200,display:"flex"}}),r.a.createElement("center",null,r.a.createElement(p.a,{className:t.text,variant:"h5"},e.children))))}function Ee(){var e=Object(i.c)((function(e){return e.loading})),t=ie();return r.a.createElement(re.a,{className:t.backdrop,open:e>0},r.a.createElement(ce,null,r.a.createElement(oe.a,{color:"inherit"})))}var _e=a(167),se=Object(l.a)((function(e){return{content:{flexGrow:1,transition:e.transitions.create("margin",{easing:e.transitions.easing.sharp,duration:e.transitions.duration.leavingScreen}),display:"flex",minHeight:"calc(100vh - 45px)"},contentShift:{transition:e.transitions.create("margin",{easing:e.transitions.easing.easeOut,duration:e.transitions.duration.enteringScreen})},main:{width:"100%",padding:e.spacing(10,3),borderRadius:0}}}));function le(e){var t,a,n=Object(i.c)((function(e){return e.error})),o=Object(i.b)(),c=se();return n.show&&o((t=n.status,a="error",function(e){return e({type:E.s,message:t,messageType:a})})),r.a.createElement("main",{className:Object(N.a)(c.content,Object(P.a)({},c.contentShift,e.drawerOpen))},r.a.createElement("div",{className:c.main},r.a.createElement(r.a.Fragment,null,r.a.createElement(Ee,null),r.a.createElement(_e.c,null,r.a.createElement(_e.a,{exact:!0,path:"/overview",component:ee}),r.a.createElement(_e.a,{path:"/",component:ee})))))}var Re=a(3),de=Object(l.a)((function(e){var t;return{profileBox:{backgroundColor:e.palette.primary.darkGray,width:90,height:90,marginBottom:5},profileTypography:{textAlign:"center",marginTop:"18px",fontWeight:"bold",color:e.palette.text.primary},profilePaper:{borderRadius:"50%",width:"60px",height:"60px",backgroundColor:e.palette.primary.lightGray},list:{height:"100%"},logoutListItem:{position:"absolute",bottom:40},imgSize:{width:"80%"},iconTypography:{textAlign:"center",paddingTop:3},iconPaper:{borderRadius:"50%",width:"50px",height:"50px",backgroundColor:"inherit"},iconPaperActive:{backgroundColor:e.palette.primary.main},drawer:{width:90,flexShrink:0,whiteSpace:"nowrap",zIndex:e.zIndex.appBar-1,paddingTop:60},drawerOpen:{width:90,backgroundColor:e.palette.primary.dark,zIndex:e.zIndex.appBar-1,transition:e.transitions.create("width",{easing:e.transitions.easing.sharp,duration:e.transitions.duration.enteringScreen}),paddingTop:60},drawerClose:(t={transition:e.transitions.create("width",{easing:e.transitions.easing.sharp,duration:e.transitions.duration.leavingScreen}),overflowX:"hidden",zIndex:e.zIndex.appBar-1,width:e.spacing(7)+1},Object(P.a)(t,e.breakpoints.up("sm"),{width:e.spacing(7)+1}),Object(P.a)(t,"paddingTop",5),t),toolbar:Object(Re.a)({display:"flex",alignItems:"center",justifyContent:"flex-end",padding:e.spacing(0,1)},e.mixins.toolbar)}})),Se=a(283),ue=a(272),me=a(277),pe=a(282),Oe=a(278),ge=a(229),Te=a.n(ge);function fe(e){var t,a,n=Object(_e.f)(),o=de(),i=n.location.pathname;return r.a.createElement(Se.a,{anchor:"left",variant:"permanent",className:Object(N.a)(o.drawer,(t={},Object(P.a)(t,o.drawerOpen,e.drawerOpen),Object(P.a)(t,o.drawerClose,!e.drawerOpen),t)),classes:{paper:Object(N.a)((a={},Object(P.a)(a,o.drawerOpen,e.drawerOpen),Object(P.a)(a,o.drawerClose,!e.drawerOpen),a))},open:e.drawerOpen},r.a.createElement(me.a,{className:o.list},r.a.createElement(h.a,{container:!0,justify:"center",alignItems:"center",className:o.profileBox},r.a.createElement(h.a,{item:!0,xs:12},r.a.createElement(pe.a,{key:"user_image"},r.a.createElement(Oe.a,null,r.a.createElement(ue.a,{className:o.profilePaper},r.a.createElement(p.a,{className:o.profileTypography},"TESTER")))))),r.a.createElement(pe.a,{button:!0,onClick:function(){return n.replace("/overview")},key:"overview"},r.a.createElement(Oe.a,null,r.a.createElement(ue.a,{className:Object(N.a)(o.iconPaper,Object(P.a)({},o.iconPaperActive,"/overview"===i))},r.a.createElement(p.a,{className:o.iconTypography},r.a.createElement("img",{src:Te.a,className:o.imgSize,alt:"Overview"})))))))}var Pe=a(230),Ne=a.n(Pe),he={dark:Ne()({palette:{type:"dark",primary:{main:"rgb(85,85,85)",dark:"rgb(166,166,166)"},success:{main:"#bac778"},action:{selected:"#009c82"}},overrides:{MuiPaper:{root:{backgroundColor:"rgb(166,166,166)"}},MuiAppBar:{root:{backgroundColor:"rgb(85,85,85)"}}}}),light:Ne()({palette:{type:"light",text:{primary:"rgb(255,255,255)",secondary:"rgb(100,100,100)"},primary:{light:"#4CACC1",main:"#008AA8",dark:"#00242C",darkGray:"#525252",lightGray:"#A9A8A8",lighterGray:"rgb(200,200,200)",white:"#ffffff",black:"#000000",boxShadow:"4px 4px #A9A8A8"},secondary:{light:"rgb(255,255,255)",main:"rgb(255,255,255)",dark:"rgb(255,255,255)"},action:{selected:"rgb(166,166,166)"}},overrides:{MuiAppBar:{root:{backgroundColor:"#008AA8"}}}})},Ae=Object(l.a)((function(e){return{root:{display:"flex",minHeight:e.spacing(7)}}})),be=a(279);function ve(){var e=Ae(),t=Object(i.c)((function(e){return"dark"===e.theme?he.dark:he.light}));return r.a.createElement(s.a,{theme:t},r.a.createElement(c.SnackbarProvider,{maxSnack:5},r.a.createElement(_,null),r.a.createElement(o.a,null,r.a.createElement("div",{className:e.root},r.a.createElement(be.a,null),r.a.createElement(O,null),r.a.createElement(fe,{keepMounted:!0,drawerOpen:!0}),r.a.createElement(le,{drawerOpen:!0})))),r.a.createElement(f,null))}a.d(t,"default",(function(){return ve}))}}]);
//# sourceMappingURL=4.8c61d61f.chunk.js.map
float2 p=UV.xy;
float Seed=UV.z;
float Age=UV.w;
float Stroke=.018;
int g=min(4,(int)floor(saturate(Seed)*5.0));
float4 lines[6];
lines[0]=float4(.50,.12,.50,.88);
lines[1]=float4(.50,.16,.78,.36);
lines[2]=float4(.78,.36,.50,.54);
lines[3]=float4(.50,.56,.25,.76);
lines[4]=float4(.50,.42,.25,.22);
lines[5]=float4(.50,.68,.76,.86);
if(g==1){
lines[0]=float4(.24,.16,.24,.86);
lines[1]=float4(.76,.16,.76,.86);
lines[2]=float4(.24,.28,.76,.70);
lines[3]=float4(.24,.70,.76,.28);
lines[4]=float4(.50,.12,.50,.28);
lines[5]=float4(.50,.72,.50,.88);
}else if(g==2){
lines[0]=float4(.50,.12,.50,.88);
lines[1]=float4(.22,.37,.50,.14);
lines[2]=float4(.50,.14,.78,.37);
lines[3]=float4(.22,.62,.50,.40);
lines[4]=float4(.50,.40,.78,.62);
lines[5]=float4(.34,.78,.66,.78);
}else if(g==3){
lines[0]=float4(.48,.12,.48,.88);
lines[1]=float4(.48,.15,.76,.35);
lines[2]=float4(.76,.35,.48,.54);
lines[3]=float4(.48,.54,.76,.75);
lines[4]=float4(.76,.75,.48,.88);
lines[5]=float4(.48,.42,.23,.60);
}else if(g==4){
lines[0]=float4(.22,.50,.50,.16);
lines[1]=float4(.50,.16,.78,.50);
lines[2]=float4(.78,.50,.50,.84);
lines[3]=float4(.50,.84,.22,.50);
lines[4]=float4(.50,.12,.50,.88);
lines[5]=float4(.22,.50,.78,.50);
}
float d=2.0;
[unroll]for(int i=0;i<6;i++){
float2 a=lines[i].xy,b=lines[i].zw;
float2 ab=b-a;
float t=saturate(dot(p-a,ab)/max(dot(ab,ab),.00001));
d=min(d,length(p-a-ab*t));
}
float aa=max(fwidth(d),.0015);
float mask=1.0-smoothstep(Stroke-aa,Stroke+aa,d);
float fade=smoothstep(0.0,.12,Age)*(1.0-smoothstep(.76,1.0,Age));
return saturate(mask*fade);

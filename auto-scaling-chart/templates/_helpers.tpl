{{/*
Selector labels
*/}}
{{- define "helper.labels" -}}
{{- $app := index . "app"  -}}
{{- $component := index . "component" -}}
app: $app
component: $component
{{- end -}}
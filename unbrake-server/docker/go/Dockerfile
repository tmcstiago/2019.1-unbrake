# Build the code in a alpine distro
FROM golang:1.12.4-alpine3.9 AS builder

WORKDIR /home

ADD src/ .

RUN go build main.go

# Run the code in alpine 
FROM alpine:3.9 AS runner

WORKDIR /home

COPY --from=builder /home/main /home

CMD ./main

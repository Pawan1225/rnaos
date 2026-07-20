FROM node:22

WORKDIR /app

COPY . .

RUN npm install -g pnpm
RUN pnpm install

EXPOSE 3000

CMD ["pnpm", "dev", "--hostname", "0.0.0.0"]

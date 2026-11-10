export default {
	async fetch(request, env) {
		if (!env.BLOG) {
			return new Response("Blog service binding is not configured.", { status: 500 });
		}
		return env.BLOG.fetch(request);
	},
};

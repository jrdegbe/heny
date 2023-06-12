public class RecommendationServiceAPI {
    private RecommendationService recommendationService;

    public RecommendationServiceAPI(RecommendationService recommendationService) {
        this.recommendationService = recommendationService;
    }

    @GET
    @Path("/recommendations/{userId}")
    public Response getRecommendations(@PathParam("userId") String userId) {
        List<Recommendation> recommendations = recommendationService.getRecommendations(userId);
        return Response.ok(recommendations).build();
    }
}